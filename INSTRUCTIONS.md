# Movie Explorer Platform - Project Guide

## Objective

Create a **Movie Explorer Platform** that allows users to explore movies, actors, directors, and genres. There is no
need for user authentication (i.e., login/signup).

---

## Backend Requirements

### Technologies to Use:

- **Backend Framework**: Python-based (e.g., **Flask** or **FastAPI**).
- **Database**: Any database of your choice (e.g., **SQLite**, **PostgreSQL**, or **MongoDB**).
- **API Documentation**: Use **Swagger** with **OpenAPI** specifications to document your API.

### Core Entities and API Resources:

You need to implement the following entities and API endpoints:

1. **Movies**
2. **Actors**
3. **Directors**
4. **Genres**

### Relationships Between Models:

- A **movie** can belong to multiple **genres**.
- A **movie** can have multiple **actors** and a **single director**.

### API Filtering:

You should allow users to filter or search:

- **Movies** by:
    - Genre
    - Director
    - Release year
    - Actor
- **Actors** by:
    - Movies they’ve acted in
    - Genres they’ve acted in

### Example API Endpoints:

- `/movies` – List of movies (can filter by genre, actor, director).
- `/actors` – List of actors (can filter by movies or genres).
- `/directors` – List of directors.
- `/genres` – List of genres.

---

## Frontend Requirements

### Technologies to Use:

- **Frontend Framework**: Choose between **ReactJS** or **VueJS** (using **TypeScript** is highly recommended, but *
  *JavaScript** is also okay).
- **CSS Framework**: You can use any CSS framework, such as **Tailwind CSS**, **Bootstrap**, or **Material UI**.

### User Interface Features:

Your platform should allow users to:

1. **Browse Movies**:
    - Display a list of movies with key details (e.g., title, release year, genres, director).
2. **Filter/Search Movies**:
    - Allow users to filter movies by **genre**, **actor**, or **director**.
3. **Movie Detail Page**:
    - Show a detailed view of each movie, including the cast, director, and genres.
4. **Actor/Director Profile Page**:
    - Show a profile page for each actor and director, displaying the movies they have worked on.

---

## Project Expectations

### What You Need to Submit:

- **Full-stack Application**: A working application with both frontend and backend.
- **Clear README.md**: Document your project and provide clear instructions on how to run the app.
- **Docker**: Containerize your app (both frontend and backend) with **Docker**. Provide Docker build and run commands.
- **Vite for Frontend**: Use **Vite** as the bundler for your frontend project (it’s fast and simple to use).
- **Code Linting**: Integrate **linting** into the build step to ensure clean and consistent code.
- **Unit Tests**: Write **unit tests** for both the backend and frontend, and integrate them into the build process.

### Backend Guidelines:

- All **data filtering** should be handled **on the backend**. The frontend should only request the filtered data, not
  handle the filtering itself.

---

## General Guidelines

- **Push your code to GitHub**: Your project should be in a **public GitHub repository**. Include all files necessary to
  run the app.
- **Movie Ratings/Reviews**: Add **mock data** for movie ratings or reviews (even if it's not connected to a user
  system).
- **Edge Cases**: Handle cases like **no movies available**, **invalid filters**, or **empty search results**.
- **Maintainable Code**: Write clean, modular, and maintainable code that follows best practices.
- **Good UI/UX**: Make sure the design is user-friendly and follows good UI/UX principles.

---

## Bonus (Optional)

- **Favorites/Watch Later**: Implement a "favorites" or "watch later" section where users can save movies. This doesn’t
  require a user authentication system. You can store this data using **local storage** in the browser.

---

## Final Notes

- Make sure your app is **fully functional** and **well-tested**.
- Provide **clear documentation** in your README.md file so others (like your evaluators) can easily set up and run your
  project.
- Follow the **coding standards** and make your code easy to understand.

Good luck, and have fun building the platform!

---
