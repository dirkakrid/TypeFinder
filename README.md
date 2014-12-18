# TypeFinder
========

Utility to recognize types in text for data wrangling purposes

## Example
### Code
```python
import typefinder

text = 'vlan-12 in 1.2.3.4'

for t in typefinder.all_types:
    matches = t.search(text)
    if matches:
        print t.what, matches
```
### Output
```
ipv4.ip [u'1.2.3.4']
vlan [12]
```
