# To-Do List Manager

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: PEP 8](https://img.shields.io/badge/Code%20Style-PEP%208-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

A feature-rich console-based to-do list manager built with Python, featuring persistent storage, search functionality, and a professional CLI interface with object-oriented design.

## 🎯 Project Overview

This To-Do List application showcases professional Python development practices through a comprehensive task management system. Built with object-oriented principles, the application provides persistent file storage, advanced search capabilities, and an intuitive command-line interface suitable for daily productivity management.

### ✨ Key Features

- **Complete CRUD Operations**: Add, view, update, delete tasks  
- **Persistent Storage**: Automatic file-based data persistence  
- **Task Status Management**: Mark tasks as pending or completed  
- **Advanced Search**: Find tasks by keyword with case-insensitive matching  
- **Statistics Dashboard**: Track completion rates and productivity metrics  
- **Professional Interface**: Clean CLI with visual indicators and formatting  
- **Data Integrity**: Robust error handling and data validation  
- **Auto-incrementing IDs**: Unique task identification system  

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher  
- Terminal/Command Prompt  
- File system write permissions  

### Installation & Usage

1. **Clone this repository**

   git clone https://github.com/Awaissyed12/To-Do-List-Manager.git
   
   cd python-todo-list-manager


3. **Install required packages**
   
   python todo.py
   
5. **Follow the interactive interface:**

============================================================ 

📝 TO-DO LIST MANAGER

1. 📝 Add Task

2. 👀 View All Tasks

3. 👁️ View Pending Tasks Only

4. ✅ Mark Task as Complete

5. 🗑️ Remove Task

6. 🔍 Search Tasks

7. 📊 Show Statistics
8. 🚪 Exit

## 💻 Usage Examples

### Adding and Managing Tasks

Enter your choice (1-8): 1

📝 Adding New Task 

Enter task description: Complete Python project documentation 

✅ Task added successfully! (ID: 1) 

💾 Tasks saved to tasks.txt 

### Viewing Tasks 

================================================================================ 

📝 TO-DO LIST 

ID Task Status Date Added 

1 Complete Python project documentation ⏳ Pending 2025-09-24 20:25:30 

2 Review code implementation ✅ Completed 2025-09-24 20:30:15 

📊 Total: 2 | Pending: 1 | Completed: 1 

### Search Functionality

🔍 Enter search keyword: Python 

🔍 Search results for 'Python': 

ID 1: Complete Python project documentation [⏳ Pending]


## 🏗️ Project Structure

python-todo-list-manager/ 

├── todo.py # Main application file

├── tasks.txt # Data storage file (auto-generated)

├── README.md # Project documentation

├── screenshots/ # Application screenshots

│ ├── main-interface.png

│ ├── task-management.png

│ ├── search-demo.png

│ └── statistics-view.png

└── docs/

└── task2-submission.pdf # Complete documentation

## ⚙️ Technical Implementation

**File Storage Format:**

1|Complete Python project documentation|Pending|2025-09-24 20:25:30 

2|Review code implementation|Completed|2025-09-24 20:30:15 

3|Prepare presentation slides|Pending|2025-09-24 20:35:45 

- **Format**: `ID|Task Description|Status|Date Added`

- **Delimiter**: Pipe (|) character for reliable parsing
  
- **Encoding**: UTF-8 for international character support
 
- **Auto-save**: Every operation automatically persists data
  

### Core Functionality

| Feature           | Implementation                 | Benefits                 |  
| ----------------- | ------------------------------| ------------------------|  
| **Task Storage**  | List-based in-memory management| Fast access and manipulation |  
| **File Persistence** | Custom pipe-delimited format   | Human-readable, reliable |  
| **Error Handling** | Try/catch blocks throughout    | Graceful failure recovery|  
| **Input Validation** | Multi-layer validation system | Prevents data corruption  |  
| **Search Engine**  | Case-insensitive keyword matching | Flexible task discovery  |  

## 🔧 Advanced Features

### Professional Enhancements

- **Visual Indicators:** Emojis and formatting for better UX  
- **Statistics Dashboard:** Real-time productivity analytics  
- **Confirmation Dialogs:** Safety prompts for destructive operations  
- **Data Recovery:** Handles corrupted or missing data files  
- **Type Hints:** Modern Python typing for code documentation  
- **Comprehensive Logging:** Detailed operation feedback  

### Data Management

- **Atomic Operations:** Each action commits immediately  
- **Data Integrity:** Validation at input and storage levels  
- **Backup Safety:** Graceful handling of file system errors  
- **Unicode Support:** Full international character compatibility  

## 📊 Features Demonstration

### Core Requirements Met ✅

- [x] Lists to store tasks  
- [x] Add/Remove/View functionality  
- [x] Store tasks in text file using `open()`  
- [x] Persistent CLI to-do app  

### Professional Enhancements ✅

- [x] Object-oriented design with proper encapsulation  
- [x] Advanced search and filtering capabilities  
- [x] Statistics and analytics dashboard  
- [x] Professional CLI with visual feedback  
- [x] Comprehensive error handling and data validation  
- [x] Auto-incrementing ID system and timestamp tracking  

## 🛠️ Development Practices

### Software Engineering Standards

- **Object-Oriented Design:** Proper encapsulation and single responsibility  
- **SOLID Principles:** Clean architecture and maintainable code  
- **Type Safety:** Comprehensive type hints for better code quality  
- **Error Resilience:** Exception handling for all operations  
- **Code Documentation:** Detailed docstrings and inline comments  

### Agile Development Methodology

- **User-Centered Design:** Interface focused on user experience  
- **Iterative Enhancement:** Core features first, advanced features added  
- **Quality Assurance:** Extensive testing of edge cases and error conditions  
- **Professional Execution:** Production-ready code suitable for team development  

## 📈 Performance & Scalability

### Efficiency Features

- **Memory Management:** Efficient list operations and data structures  
- **File I/O Optimization:** Minimal disk operations with batch processing  
- **Search Performance:** Optimized keyword matching algorithms  
- **UI Responsiveness:** Clean interface with minimal loading times  

### Scalability Considerations

- **Modular Design:** Easy to extend with additional features  
- **Data Format:** Simple format that scales with data growth  
- **Error Recovery:** Robust handling of large datasets and file corruption  

## 🧪 Testing & Quality Assurance

### Test Scenarios Covered

- ✅ Adding tasks with various descriptions and edge cases  
- ✅ Removing tasks by valid and invalid IDs  
- ✅ Marking tasks as complete and status management  
- ✅ Search functionality with different keywords and patterns  
- ✅ File persistence across application sessions  
- ✅ Error handling for corrupted data and file system issues  

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Awais Syed**  
- 🔗 GitHub: [@AwaisSyed12](https://github.com/AwaisSyed12)  
- 📧 Email: [awaissyed1212@gmail.com](mailto:awaissyed1212@gmail.com)  
- 💼 LinkedIn: [Awais Syed](https://linkedin.com/in/awais-syed-686b46376)   

## 🙏 Acknowledgments

- Built as part of Python Developer role technical assessment  
- Demonstrates proficiency in Python fundamentals and object-oriented programming  
- Showcases software engineering best practices and professional development standards  
- Thanks to the Python community for excellent documentation and best practices  

## 🔮 Future Enhancements

- [ ] Due date functionality with reminders  
- [ ] Priority levels and task categorization  
- [ ] Export functionality (JSON, CSV formats)  
- [ ] Multi-user support with authentication  
- [ ] Web interface integration  
- [ ] Task synchronization across devices  

---

⭐ **Star this repository if you found it helpful!**

🚀 **Ready to boost your productivity? Give it a try and let me know what you think!**
