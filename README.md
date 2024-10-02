# Python Programming 

## Overview

This project is a collection of data structures and algorithms implemented in Python, along with some utility applications such as a Todo List and an Expense Tracker. Each module demonstrates fundamental programming concepts, showcasing how to effectively manage data and perform operations.

## Directory Structure

```plaintext
.
├── .github
│   └── workflows
│       └── pylint.yml         # GitHub Actions configuration for code linting
├── DSA
│   ├── dynamic_array.py        # Implementation of a dynamic array
│   ├── intqueue.py             # Implementation of an integer queue
│   ├── intstack.py             # Implementation of an integer stack
│   ├── linkedlist.py           # Implementation of a linked list
│   ├── queue.py                # Generic queue implementation
│   ├── stack.py                # Generic stack implementation
│   ├── static_array.py         # Implementation of a static array
├── Todo_list.py                # A simple command-line Todo List application
├── expense_tracker.py          # A command-line Expense Tracker
├── expense_tracker_gui.py      # GUI-based Expense Tracker
└── README.md                   # Project overview and documentation

```
## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```
2.Install the required dependencies:
   ```bash
pip install -r requirements.txt
```
### Linting
The project uses Pylint for code quality checks. To run linting, you can use the GitHub Actions configuration in .github/workflows/pylint.yml, or run it locally with:
```bash
pylint DSA/ Todo_list.py expense_tracker.py expense_tracker_gui.py
```
## Contributing

Contributions are welcome! Please follow these guidelines for contributing:
- Fork the repository and create a new branch for your changes.
- Ensure your code adheres to the coding standards outlined in the project.
- Write tests for new features or bug fixes.
- Submit a pull request with a clear description of your changes.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [22wh1a12b5@bvrithyderabad.edu.in](mailto:22wh1a12b5@bvrithyderabad.edu.in).
