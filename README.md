# mdprint

Python tools to print strings to markdown file with styles. Also allows printing dicts and lists to table

## Installation

```
pip install mdprint
```
## Quick Start

### Basics

```
mdprint('Markdown styles', heading=3)
mdprint('It is convenient to use mdprint just like print.\n')
mdprint('You can make text ', end='')
mdprint('bold', bold=True, end=', ')
mdprint('italics', italics=True, end=', ')
mdprint('or even ', end='')
mdprint('strikethrough', strikethrough=True)
mdprint('\nYou can also write ', end='')
mdprint('code', code=True)
mdprint('from mdprint import mdprint', code_block=True)
```

### Markdown styles
It is convenient to use mdprint just like print.

You can make text **bold**, _italics_, or even ~~strikethrough~~

You can also write `code`

```
from mdprint import mdprint
```

### Writing to file

mdprint takes `file` argument similar to `print`

```
with open('README.md', 'w') as f:
    mdprint('Hello', heading=2, file=f)
```

### Dict
```
from mdprint import mdprint_dict
mydict = {'dogs': ['goldie', 'labrador', 'bulldog'], 'cats': ['polydactyl', 'snowshoe', 'calico'], 'fish': ['cod', 'herring', 'mackerel']}
```

```
mdprint_dict(mydict)
```

| dogs | cats | fish |
|----|----|----|
| goldie | polydactyl | cod |
| labrador | snowshoe | herring |
| bulldog | calico | mackerel |

### List

```
from mdprint import mdprint_list
mylist = [['goldie', 'labrador', 'bulldog'], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
```

```
mdprint_list(mylist)
```

| goldie | labrador | bulldog |
|----|----|----|
| 4 | 5 | 6 |
| 7 | 8 | 9 |
| 10 | 11 | 12 |

### Advanced

You can sort, invert and combine commands

```
mdprint_list([['animal type', 'variety 1', 'variety 2', 'variety 3']], end='')
mdprint_dict(b, keys_as_headers=False, sort_keys=True, start='')
```

| animal type | variety 1 | variety 2 | variety 3 |
|----|----|----|----|
| *cats* | polydactyl | snowshoe | calico |
| *dogs* | goldie | labrador | bulldog |
| *fish* | cod | herring | mackerel |


## Contributing

Pull requests are very welcome.

1. Fork the repo
1. Create new branch with feature name as branch name
1. Check if things work with a jupyter notebook
1. Raise a pull request

## Licence

Please see attached [Licence](LICENCE)
