# Movie Explorer Platform

A full-stack web application that allows film enthusiasts to explore movies, actors, directors, and genres. Built with
FastAPI (Python) backend and React (JaveScript) frontend.

## 🎬 Features

### Backend

- RESTful API built with FastAPI
- SQLite database with well-defined relationships
- Comprehensive filtering capabilities:
    - Movies by genre, director, release year, or actor
    - Actors by movies or genres
- Interactive API documentation with Swagger/OpenAPI
- Unit tests and linting integrated
- Dockerized for easy deployment

### Frontend

- Modern React application with TypeScript
- Responsive UI with CSS framework
- Key functionality:
    - Browse movies with details (title, release year, genres, director)
    - Advanced filtering and search (genre, actor, director)
    - Detailed movie pages with full cast and crew information
    - Actor/Director profile pages with filmography
    - Movie ratings and reviews
    - Favorites/Watch Later feature (using local storage)
- Unit tests and linting integrated
- Built with Vite for optimal performance

## 🏗️ Architecture

### Database Schema

- **Movies**: Core entity with title, release year, rating, and description
- **Actors**: Artist profiles with biographical information
- **Directors**: Filmmaker profiles with career details
- **Genres**: Movie categories and classifications
- **Relationships**:
    - Many-to-Many: Movies ↔ Genres, Movies ↔ Actors
    - One-to-Many: Directors → Movies

## 🚀 Getting Started

### Prerequisites

- Docker installed on your system
- Git for cloning the repository

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jeetendra29gupta/Movie-Explorer-Platform.git
   cd Movie-Explorer-Platform
   ```

2. **Build and Run the Backend Container**
   ```bash
   docker build -t movie-explorer-backend ./backend
   docker run -d -p 8181:8181 --name movie-explorer-backend movie-explorer-backend
   ```

3. **Build and Run the Frontend Container**
   ```bash
   docker build -t movie-explorer-frontend ./frontend
   docker run -d -p 9191:9191 --name movie-explorer-frontend movie-explorer-frontend
   ```

### Access the Application

- **Frontend UI**: [http://localhost:9191/](http://localhost:9191/)
- **Backend API**: [http://localhost:8181/](http://localhost:8181/)
- **API Documentation**: [http://localhost:8181/docs](http://localhost:8181/docs)
- **Alternative API Docs**: [http://localhost:8181/redoc](http://localhost:8181/redoc)

## 🛠️ Development

### Running Locally Without Docker

#### Backend

```bash
cd backend

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

python --version
pip --version

pip install -r requirements-dev.txt

pytest
black app/ tests/  --line-length 90
flake8 app/ tests/ --max-line-length 90

uvicorn app.main:app --reload --host '0.0.0.0' --port 8181
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Building for Production

#### Backend

```bash
cd backend
docker build -t movie-explorer-backend .
```

#### Frontend

```bash
cd frontend
docker build -t movie-explorer-frontend .
npm run build  # Creates production build
```

## 📚 API Endpoints

### Movies

- `GET /api/movies` - List all movies with filtering options
    - Query params: `genre`, `director`, `actor`, `year`
- `GET /api/movies/{id}` - Get movie details
- `POST /api/movies` - Create a new movie
- `PUT /api/movies/{id}` - Update movie
- `DELETE /api/movies/{id}` - Delete movie

### Actors

- `GET /api/actors` - List all actors with filtering
    - Query params: `movie`, `genre`
- `GET /api/actors/{id}` - Get actor profile with filmography
- `POST /api/actors` - Create actor
- `PUT /api/actors/{id}` - Update actor
- `DELETE /api/actors/{id}` - Delete actor

### Directors

- `GET /api/directors` - List all directors
- `GET /api/directors/{id}` - Get director profile with filmography
- `POST /api/directors` - Create director
- `PUT /api/directors/{id}` - Update director
- `DELETE /api/directors/{id}` - Delete director

### Genres

- `GET /api/genres` - List all genres
- `GET /api/genres/{id}` - Get genre with associated movies
- `POST /api/genres` - Create genre
- `PUT /api/genres/{id}` - Update genre
- `DELETE /api/genres/{id}` - Delete genre

## 🧪 Testing

### Backend Tests

```bash
cd backend
python -m pytest --cov=app tests/
```

### Frontend Tests

```bash
cd frontend
npm run test
npm run test:coverage
```

## 📦 Project Structure

```
Movie-Explorer-Platform/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── routes/          # API endpoints
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── database.py      # Database configuration
│   │   └── main.py          # FastAPI application
│   ├── tests/               # Backend unit tests
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API service layer
│   │   ├── hooks/           # Custom React hooks
│   │   └── App.tsx          # Main application
│   ├── tests/               # Frontend unit tests
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.ts
└── README.md
```

## 🎯 Features Implemented

### Core Requirements

- ✅ Full CRUD operations for all entities
- ✅ Meaningful relationships between models
- ✅ Backend filtering (not frontend)
- ✅ Swagger/OpenAPI documentation
- ✅ Dockerized application
- ✅ Unit tests for both frontend and backend
- ✅ Linting integrated in build process
- ✅ Vite as frontend bundler
- ✅ TypeScript for type safety

### Bonus Features

- ✅ Movie ratings and reviews
- ✅ Favorites/Watch Later functionality (local storage)
- ✅ Responsive design
- ✅ Loading states and error handling
- ✅ Comprehensive edge case handling

## 🐛 Error Handling

The application handles various edge cases:

- No movies/actors/directors available
- Invalid filter parameters
- Network errors
- Invalid data submissions
- Database connection issues
- 404 Not Found for non-existent resources

## 🔧 Technologies Used

### Backend

- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Testing**: pytest
- **Linting**: pylint
- **Documentation**: Swagger/OpenAPI

### Frontend

- **Framework**: React 18
- **Language**: TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS / Material UI / Bootstrap
- **Testing**: Vitest / Jest + React Testing Library
- **Linting**: ESLint
- **HTTP Client**: Axios / Fetch API

## 📝 Code Quality

- Modular and maintainable code structure
- Inline documentation where necessary
- Type safety with TypeScript (frontend) and Pydantic (backend)
- Comprehensive unit test coverage
- Linting enforced in build process
- RESTful API design patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Jeetendra Gupta**

- GitHub: [@jeetendra29gupta](https://github.com/jeetendra29gupta)

## 🙏 Acknowledgments

- Movie data sourced from [TMDB API / OMDb API / Custom Dataset]
- Icons and images from [source]
- Inspired by popular movie platforms like IMDb and Letterboxd

---

**Note**: This is a demonstration project built for educational purposes. All movie data, ratings, and reviews are
mock/dummy data for demonstration purposes only.