Movies = [
    {
        "id": 1,
        "title": "Inception",
        "genre": "Sci-Fi",
        "year": 2010,
        "rating": 8.8
    },
    {
        "id": 2,
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "year": 1994,
        "rating": 9.3
    },
    {
        "id": 3,
        "title": "The Godfather",
        "genre": "Crime",
        "year": 1972,
        "rating": 9.2
    },
    {
        "id": 4,
        "title": "The Dark Knight",
        "genre": "Action",
        "year": 2008,
        "rating": 9.0
    },
    {
        "id": 5,
        "title": "Pulp Fiction",
        "genre": "Crime",
        "year": 1994,
        "rating": 8.9
    }
]

Users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "role_id": 1
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "password": "securepass456",
        "role_id": 2
    }
]

Roles = [
    {
        "id": 1,
        "name": "admin"
    },
    {
        "id": 2,
        "name": "user"
    }
]

Rating = [
    {
        "id": 1,
        "user_id": 1,
        "movie_id": 1
    },
    {
        "id": 2,
        "user_id": 1,
        "movie_id": 2
    },
    {
        "id": 3,
        "user_id": 2,
        "movie_id": 3
    },
    {
        "id": 4,
        "user_id": 2,
        "movie_id": 4
    }
]