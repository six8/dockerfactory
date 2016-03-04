from schematics.models import Model
from schematics.types import *
from schematics.types.compound import ListType, DictType


class DockerFactoryConf(Model):
    """
    Configuration for Docker build

    Corresponds to https://docs.docker.com/engine/reference/commandline/build/
    """

    # --- Dockerfactory options

    # A dictionary of {source: destination} paths for the build context
    context = DictType(StringType)
    # Specify dockerfile
    dockerfile = StringType(default='./Dockerfile')

    # --- Docker build options

    # Set build-time variables
    build_arg = ListType(StringType)
    # CPU shares (relative weight)
    cpu_shares = IntType()
    # Optional parent cgroup for the container
    cgroup_parent = StringType()
    # Limit the CPU CFS (Completely Fair Scheduler) period
    cpu_period = IntType()
    # Limit the CPU CFS (Completely Fair Scheduler) quota
    cpu_quota = IntType()
    # CPUs in which to allow execution (0-3, 0,1)
    cpuset_cpus = StringType()
    # MEMs in which to allow execution (0-3, 0,1)
    cpuset_mems = StringType()
    # Skip image verification
    disable_content_trust = BooleanType()
    # Always remove intermediate containers
    force_rm = BooleanType()
    # Container isolation level
    isolation = StringType()
    # Memory limit
    memory = StringType()
    # Swap limit equal to memory plus swap: '-1' to enable unlimited swap
    memory_swap = StringType()
    # Do not use cache when building the image
    no_cache = BooleanType()
    # Always attempt to pull a newer version of the image
    pull = BooleanType()
    # Remove intermediate containers after a successful build
    rm = BooleanType()
    # Size of /dev/shm, default value is 64MB
    shm_size = StringType()
    # Name and optionally a tag in the 'name:tag' format
    tag = StringType()
    # Ulimit options
    ulimit = ListType(StringType)
