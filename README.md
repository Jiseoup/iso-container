# ISO Container
[![PyPI](https://img.shields.io/pypi/v/iso-container)](https://pypi.org/project/iso-container/)
![Python](https://img.shields.io/pypi/pyversions/iso-container)
![License](https://img.shields.io/pypi/l/iso-container)
[![CI](https://github.com/Jiseoup/iso-container/actions/workflows/ci.yml/badge.svg)](https://github.com/Jiseoup/iso-container/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/iso-container)](https://pepy.tech/projects/iso-container)

A Python package based on ISO 6346 Container Codes.  
This package provides functionalities to search for container information using ISO codes and to validate container numbers.

## Installation
Install the package using pip:
```bash
pip install iso-container
```

## Usage
### Search Container Information
You can retrieve detailed container information using an ISO code:
```python
from iso_container import get_container_info

# Example usage
container_info = get_container_info('22GP')
print(container_info)
# -> {'class': '20 GENERAL PURPOSE CONTAINER', 'type': 'STANDARD DRY', 'length': 20, 'height': 8.5}
```

### Validate Container Numbers
Validate whether a container number is compliant with the ISO 6346 standard:

```python
from iso_container import validate_container

# Example usage
is_valid = validate_container('CSQU3054383')
print('Valid Container Number' if is_valid else 'Invalid Container Number')
# -> Valid Container Number
```

## API Reference
| Function | Returns |
| --- | --- |
| `get_container_info(code)` | A `dict` with container details, or `None` if the code is unknown. The lookup is case-insensitive. |
| `validate_container(number)` | `True` if the 11-character number passes the ISO 6346 check-digit rule, otherwise `False`. |

## Dataset
The dataset used in this package is derived from the [ISO-Container-Codes](https://github.com/datasets/ISO-Container-Codes) repository, processed to enhance usability.

## License
This project is licensed under the [MIT License](https://github.com/Jiseoup/iso-container/blob/main/LICENSE).
