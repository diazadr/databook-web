# Databook_Web

![Project Status](https://img.shields.io/badge/status-completed-brightgreen) [![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

**Databook_Web** is a case study project for the **NoSQL Database** course. It is developed using **Python 3.12.3**, the **Flask** framework, and **MongoDB** as the database.

## Technologies Used
- **MongoDB Atlas**: Cloud database for the application.
- **Python Flask**: Backend framework for handling CRUD operations.
- **MongoDB**: Database for storing book-related data.
- **HTML & CSS**: User interface and form styling.

## Features
- **CRUD Operations**:
  - **Create**: Add new book records.
  - **Read**: View the list of books.
  - **Update**: Modify existing book records.
  - **Delete**: Remove book records from the system.
- **Cloud Database**: Utilizes MongoDB Atlas for data storage.
- **User-Friendly Interface**: Clean and simple UI for managing books.

## Demo

### Create
- The **Create** feature allows users to add new book records.

  ![Create Record](https://github.com/user-attachments/assets/386cdb44-1e27-4bc4-802c-1a6643b37386)

### Read
- The **Read** feature displays a list of all book records.

  ![View Records](https://github.com/user-attachments/assets/932ab822-632b-4688-8ac2-0c99710ec925)

### Update
- The **Update** feature lets users modify existing book records.

  ![Update Record](https://github.com/user-attachments/assets/8fa2c476-e95c-47af-bf66-1c2d084c8547)

### Delete
- The **Delete** feature allows users to remove a book record from the system.

  ![Delete Record](https://github.com/user-attachments/assets/ff50aca5-ead6-4f57-99c0-ecad74888d0b)

## Setup

1. **Install Python 3.12.3**  
   Download Python from the [official Python website](https://www.python.org/).
2. **Clone the Repository**  
   Open your terminal and execute:
   ```bash
   git clone <repository_url>
   cd Databook_Web
   ```
3. Set up a virtual environment and activate it:
   ```
   python -m venv env
   cd env/Scripts
   activate
   cd ../..
   ```
4. Install the required Python packages:
   ```
   pip install flask pymongo
   ```
5. Run the application:
   ```
   py app.py
   ```
   
## Usage
1. Open a browser and navigate to `localhost:5000`.
2. Use the CRUD functionalities to manage book records.
3. All data is stored in MongoDB Atlas.

## Project Status
This project is **completed** and will not be further developed.

## Contributions
Feel free to submit issues or contribute by creating pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
