"""Package sysroot from a working target system for cross-compile."""

import argparse
import subprocess
import textwrap
from pathlib import Path

sync_dirs = ['lib', 'usr/include', 'usr/lib', 'usr/local/include', 'usr/local/lib']

sync_command = 'rsync -avzhe ssh --progress moonrobot:/usr/local/lib ~/src/sysroot-RPi-buster-arm7l/usr/local/ --delete'

parser = argparse.ArgumentParser(
    description='%(prog)s : Package sysroot from a working target system for cross-compile.',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent(
        """\
    This script is meant to be used to package a sysroot from a working target system
    (via rsync) and prepare it for cross-compilation. The script will sync the necessary
    directories from the target system to the output directory. The output directory will
    be packaged into the desired archival format.

        python3 scripts/package_sysroot.py -o sysroot-armv8-rpi4_bookworm-linux -v romirobot

    Written by Sterling Peet <sterling.peet@gatech.edu>
    """
    ),
)
parser.add_argument(
    'hostname',
    help='Target ssh hostname, including user if needed (e.g. user@hostname)',
)
parser.add_argument('-o, --output', dest='OUT', default='sysroot', help='Output directory')
parser.add_argument('-f, --format', dest='FORMAT', default='tar.gz', help='Package format')
parser.add_argument(
    '-v, --verbose', dest='VERBOSE', action='store_true', help='Verbose output'
)

args = parser.parse_args()

sysroot_dir = Path(args.OUT)
print(f'Sysroot directory: {sysroot_dir}')
sysroot_dir.mkdir(exist_ok=True)

# Loop through the sync_dirs and rsync them to the output directory
for sync_dir in sync_dirs:
    target_dir = sysroot_dir / sync_dir
    target_dir.parent.mkdir(exist_ok=True)
    sync_command = (
        f'rsync -avzhe ssh --progress {args.hostname}:/{sync_dir} {target_dir.parent} --delete'
    )
    if args.VERBOSE:
        print(sync_command)
    sync_cmd = sync_command.split()
    subprocess.run(sync_cmd)

# Package the sysroot directory using tar
package_name = f'{sysroot_dir.name}.{args.FORMAT}'
print(f'Packaging sysroot directory: {package_name}')
package_command = f'tar -czvf {package_name} {sysroot_dir}'
if args.VERBOSE:
    print(package_command)
package_cmd = package_command.split()
subprocess.run(package_cmd)
