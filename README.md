# BookPilot 📚📖

*Modern library management system showcasing full-stack Django expertise with a sleek, responsive UI.*

[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?style=for-the-badge&logo=postgresql)](https://supabase.com/) 
<br>
[![Jinja](https://img.shields.io/badge/Jinja-v3-B41717?style=for-the-badge&logo=jinja&logoColor=white)](https://palletsprojects.com/p/jinja/) [![HTML5](https://img.shields.io/badge/HTML5-v5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) [![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-v3-38B2AC?style=for-the-badge&logo=tailwind-css)](https://tailwindcss.com/) [![Responsive](https://img.shields.io/badge/Responsive-Yes-F97316?style=for-the-badge)](#) 

## 📋 Overview
BookPilot is a full-stack Django application designed to streamline library management with a user-friendly, responsive interface. This project demonstrates my proficiency in building secure, scalable web applications with modern technologies, featuring robust backend logic, polished frontend design, and seamless database integration. Deployed on **Render**, it highlights my ability to deliver production-ready solutions.

## 🛠 Technologies Used
- **Backend**: Django 5.2 (Core framework for routing, authentication, and logic)

- **Frontend**: HTML5, Tailwind CSS (Responsive layouts with gradient themes)

- **Database**: PostgreSQL (Hosted on Supabase for efficient data management)

- **Extras**: Crispy Forms (Bootstrap 5), Email Integration (SMTP), Atomic Transactions (Concurrency safety)

- **Deployment**: Hosted on Render.com

## 🌟 Key Features 

- **One-Click Book Borrowing & Returns**: Securely Borrow or return books instantly with real-time balance updates. 

- **User Dashboard**: Track borrow history, deposit funds, and view profiles with responsive Tailwind styling. 📊

- **Reviews & Ratings**: Share Review and Rattings(out of 5⭐) only after borrowing the Specific Book.

- **Category Filters**: Filter books by genres with sleek, mobile-friendly UI.

- **Email Notifications**: Instant alerts for Money deposits, Book borrows and returns (Gmail SMTP integrated). Vibrant, HTML-based email body.

- **Secure Transactions**: Atomic operations with PostgreSQL (via Supabase) ensure safe, concurrent data handling.


## 📸 Sneak Peek
![Home Page](https://res.cloudinary.com/dlhx7zvg3/image/upload/v1759849531/Home_page_rhgtlw.png)
![Profile Dashboard](https://res.cloudinary.com/dlhx7zvg3/image/upload/v1759849525/User_Profile_page_cxafdh.png)  
*Responsive profile page with borrow history – Responsive for all devices.*

## ⚙️ Installation & Setup
1. **Clone the repository**:
```bash
git clone https://github.com/Tasmia-Chowdhury-Alif/BookPilot-Library_Management.git
```
2. **Create & activate virtual environment**:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. **Install Dependencies**: 
```bash
pip install -r requirements.txt
```
4. **Configure Environment Variables (.env)**:
```env
SECRET_KEY=your_django_secret_key
DJANGO_DEBUG=True
DB_NAME=postgres
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_port
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
STRIPE_PUBLISHABLE_KEY=your_key
STRIPE_SECRET_KEY=your_key
STRIPE_WEBHOOK_SECRET=your_key
```

5. **Run Migrations**: 
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
🎉 **Success!** Visit [http://127.0.0.1:8000/i/](http://127.0.0.1:8000/) to explore.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Tasmia Chowdhury Alif**

- GitHub: [@Tasmia-Chowdhury-Alif](https://github.com/Tasmia-Chowdhury-Alif)
- Email: tasmiachowdhuryalif222@gmail.com

---

<div align="center">

### ⭐ If this project helped you, please give it a star!

**Built with ❤️ by Tasmia Chowdhury Alif**

[Report Bug](https://github.com/Tasmia-Chowdhury-Alif/DocEra_Health_Care/issues) • [Request Feature](https://github.com/Tasmia-Chowdhury-Alif/DocEra_Health_Care/issues)

</div>
