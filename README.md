# CrowdFunding Web Application

## Overview
The **CrowdFunding Web Application** is a web-based platform built to facilitate crowdfunding, allowing users to create, manage, and donate to fundraising projects. Inspired by platforms like GoFundMe, Kickstarter, and Crowdfunding.com, this application provides a user-friendly interface for individuals to register, log in, create fundraising campaigns, manage their projects, donate to others, and search for projects by date. The app includes robust authentication and validation features, such as Egyptian phone number validation, and is styled with modern web technologies for an engaging user experience.

The application is designed to demonstrate key web development concepts, including user authentication, project management, donation processing, and responsive design, with a focus on secure data handling and intuitive navigation.

## Features
### 1. Authentication System
- **Registration**:
  - Users can sign up by providing:
    - First name
    - Last name
    - Email (unique and validated)
    - Password (with confirmation)
    - Mobile phone (validated against Egyptian phone numbers, e.g., starting with `+201` followed by 9 digits)
- **Login**:
  - Users can log in using their email and password after successful registration.
  - Secure session management ensures authenticated access.

### 2. Project Management
- **Create a Project**:
  - Authenticated users can create fundraising campaigns with:
    - **Title**: A concise, descriptive title for the project.
    - **Details**: A detailed description of the project’s purpose.
    - **Total Target**: The fundraising goal (e.g., 250,000 EGP).
    - **Start/End Date**: Campaign duration with validated date formats (e.g., `DD/MM/YYYY`).
- **View All Projects**:
  - Users can browse a list of all projects on the platform, displayed in a responsive grid layout.
- **Edit Projects**:
  - Users can edit their own projects (title, details, target, or dates).
- **Delete Projects**:
  - Users can delete their own projects.
- **Search by Date**:
  - Users can search for projects based on their start or end dates.

### 3. Donation System
- **Donate to Projects**:
  - Users can contribute to any active project by specifying a donation amount.
  - Donations are processed securely, with validation to ensure amounts are within acceptable limits.
  - Users receive confirmation of their donation, and the project’s funding progress is updated in real-time.

## Technologies Used
- **Frontend**:
  - HTML, CSS (with Tailwind CSS for styling), JavaScript
  - Responsive design for compatibility across devices
- **Backend**:
  - Python Django 
- **Data Storage**:
  - Local file-based storage database PostgreSQL for user and project data
- **Validation**:
  - Client-side and server-side validation for emails, Egyptian phone numbers, and dates
- **External Libraries**:
  - Tailwind CSS 

## Installation

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/habibaraab/crowdfunding.git
   ```
2. Navigate to the project directory:
   ```bash
   cd crowdfunding
   ```
3. Install dependencies (if using a Python backend like django):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   - For django:
     ```bash
     python manage.py runserver
     ```
5. Open the app in your browser at `http://127.0.0.1:8000/` (or the port specified).


## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

## Inspiration
This project draws inspiration from leading crowdfunding platforms:
- [Kickstarter](https://www.kickstarter.com)
- [Crowdfunding.com](https://www.crowdfunding.com)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, please open an issue on the GitHub repository or contact the project maintainer at [habibaragab324@example.com].