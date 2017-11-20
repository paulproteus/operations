#!/usr/bin/python3
import subprocess

def name_transform(filename):
    if filename == 'README.md':
        return 'Home'

    filename = filename.rsplit('/', 1)[-1]
    filename = filename.replace('.md', '')
    from_and_to = {
        'README': 'Overview',
    }
    for key in from_and_to:
        filename.replace(key, from_and_to[key])
    return filename


def main():
    lines = sorted(
        [line.strip() for line in subprocess.check_output(['git', 'ls-files', '--', '*.md']).
         decode('utf-8').split('\n') if line.strip()],
        key=lambda s: (s.count('/'), s),
    )
    # Create a dict of dirs etc.
    created_prefixes = set()
    for line in lines:
        prefix = line.rsplit('/', 1)[0]
        if prefix == line:
            # No directory
            print('- ' + name_transform(line) + ": '" + line + "'")
        else:
            if prefix not in created_prefixes:
                print('- ' + prefix + ':')
                created_prefixes.add(prefix)
            print('    - ' + name_transform(line) + ": '" + line + "'")

if __name__ == '__main__':
    main()
