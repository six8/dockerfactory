import os
import tempfile
import click
import subprocess
from click.utils import make_str
import yaml
import tarfile
from .config import DockerFactoryConf


def _dir_to_file(ctx, param, value):
    """
    Convert value to a file if it is a directory
    """
    if os.path.isdir(value):
        value = os.path.join(value, 'Dockerfactory.yml')

    return click.File().convert(value, param, ctx)


@click.command(
    # Allow -h for help
    context_settings=dict(help_option_names=['-h', '--help']))
@click.argument(
    'file', default='.',
    type=click.Path(exists=True, resolve_path=True),
    callback=_dir_to_file,
    metavar='PATH')
@click.pass_context
def cli(ctx, file):
    """
    Docker Factory

    Utility to build Docker images with any context

    PATH: Path to Dockerfactory.yml or directory with a Dockerfactory.yml
    """
    if file.name == '-':
        # Input from stdin
        base_dir = os.getcwd()
    else:
        base_dir = os.path.dirname(file.name)

    with file as f:
        content = yaml.load(f)

    try:
        conf = DockerFactoryConf(content)
    except Exception as e:
        ctx.fail(u'Invalid Dockerfactory.yml: %s' % e)
    else:
        conf.validate(strict=True)

    # Validate context
    absolute_context = []
    for src, dst in conf.context.items():
        src = os.path.realpath(os.path.join(base_dir, src))
        if not os.path.exists(src):
            ctx.fail(u'Could not find context source "%s"' % src)
        elif not dst.startswith('/'):
            ctx.fail(u'Context destination "%s" must be an absolute path' % dst)

        absolute_context.append((src, dst))

    if conf.dockerfile:
        conf.dockerfile = os.path.realpath(os.path.join(base_dir, conf.dockerfile))
        if not os.path.exists(conf.dockerfile):
            ctx.fail(u'Could not find Dockerfile "%s"' % conf.dockerfile)

    package = tempfile.TemporaryFile()
    # Build context
    with tarfile.open(fileobj=package, mode='w:gz') as f:
        for src, dst in absolute_context:
            f.add(src, dst)

        f.add(conf.dockerfile, '/Dockerfile')

    args = []
    for k, v in conf.items():
        if k not in ('context', 'dockerfile') and v is not None:
            param_name = '--%s' % k.replace('_', '-')
            if isinstance(v, bool):
                if v is True:
                    args.append(param_name)
            else:
                args.extend((param_name, make_str(v)))

    package.seek(0)

    args = ['docker', 'build'] + args + ['-']

    click.echo(
        u'Dockerfactory building:\n'
        u'  With command: {command}\n'
        u'  With Dockerfile: {dockerfile}\n'
        u'  With context:\n    - {context}\n'.format(
            dockerfile=conf.dockerfile,
            command=' '.join(args),
            context='\n    - '.join([
                '%s: %s' % (src, dst) for src, dst in absolute_context
            ])
        )
    )

    with package:
        subprocess.check_call(
            args,
            stdin=package
        )
