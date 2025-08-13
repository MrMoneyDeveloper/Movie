#!/usr/bin/env python3
import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(description="Install dependencies and launch the demo")
    parser.add_argument("--install-only", action="store_true", help="only install npm packages")
    parser.add_argument("--no-open", action="store_true", help="do not open the browser")
    args = parser.parse_args()

    subprocess.run(["npm", "install"], check=True)

    if args.install_only:
        return

    cmd = ["npx", "vite"]
    if not args.no_open:
        cmd.append("--open")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
