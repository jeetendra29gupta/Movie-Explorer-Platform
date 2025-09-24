<script setup lang="js">
import {onMounted, ref} from 'vue';

const movies = ref([]);
const error = ref(null);

// dropdown data
const directors = ref([]);
const actors = ref([]);
const genres = ref([]);

// filter values
const selectedDirector = ref("");
const selectedActor = ref("");
const selectedGenre = ref("");
const releaseYear = ref("");

// fetch helper
async function fetchData(url, target) {
  try {
    const response = await fetch(url, {headers: {Accept: "application/json"}});
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const data = await response.json();
    target.value = data.directors || data.actors || data.genres || data.movies;
  } catch (e) {
    error.value = e.message;
    console.error("Fetch error:", e);
  }
}

async function fetchMovies() {
  let url = "http://localhost:8181/api/v1/movies?";
  const params = [];
  if (selectedDirector.value) params.push(`director_id=${selectedDirector.value}`);
  if (selectedActor.value) params.push(`actor_id=${selectedActor.value}`);
  if (selectedGenre.value) params.push(`genre_id=${selectedGenre.value}`);
  if (releaseYear.value) params.push(`release_year=${releaseYear.value}`);
  url += params.join("&");

  try {
    const response = await fetch(url, {headers: {Accept: "application/json"}});
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const data = await response.json();
    movies.value = data.movies;
  } catch (e) {
    error.value = e.message;
    console.error("Failed to fetch movies:", e);
  }
}

onMounted(async () => {
  await fetchMovies();
  await fetchData("http://localhost:8181/api/v1/directors", directors);
  await fetchData("http://localhost:8181/api/v1/actors", actors);
  await fetchData("http://localhost:8181/api/v1/genres", genres);
});

function resetFilters() {
  selectedDirector.value = "";
  selectedActor.value = "";
  selectedGenre.value = "";
  releaseYear.value = "";
  fetchMovies();
}

</script>

<template>
  <section>
    <h3 class="w3-center">Movies</h3>

    <div class="w3-row-padding w3-section w3-stretch w3-center">
      <form @submit.prevent="fetchMovies">
        <div class="w3-col w3-padding" style="width:18%">
          <button
              class="w3-button w3-block w3-border w3-round w3-light-grey"
              type="button"
              @click.prevent="resetFilters"
          >
            Reset
          </button>
        </div>

        <div class="w3-col w3-padding" style="width:16%">
          <select v-model="selectedDirector" class="w3-select w3-center w3-border w3-round w3-light-grey">
            <option value="" disabled selected>Choose director</option>
            <option v-for="director in directors" :key="director.id" :value="director.id">
              {{ director.name }}
            </option>
          </select>
        </div>
        <div class="w3-col w3-padding" style="width:16%">
          <select v-model="selectedActor" class="w3-select w3-center w3-border w3-round w3-light-grey">
            <option value="" disabled selected>Choose actor</option>
            <option v-for="actor in actors" :key="actor.id" :value="actor.id">
              {{ actor.name }}
            </option>
          </select>
        </div>
        <div class="w3-col w3-padding" style="width:16%">
          <select v-model="selectedGenre" class="w3-select w3-center w3-border w3-round w3-light-grey">
            <option value="" disabled selected>Choose genre</option>
            <option v-for="genre in genres" :key="genre.id" :value="genre.id">
              {{ genre.name }}
            </option>
          </select>
        </div>
        <div class="w3-col w3-padding" style="width:16%">
          <input
              v-model="releaseYear"
              class="w3-input w3-center w3-border w3-round w3-light-grey"
              type="text"
              placeholder="Release year"
          />
        </div>
        <div class="w3-col w3-padding" style="width:18%">
          <button
              class="w3-button w3-block w3-border w3-round w3-light-grey"
              type="submit"
          >
            Filter Movie
          </button>
        </div>
      </form>
    </div>
    <hr>

    <div class="w3-row-padding w3-section w3-stretch w3-center">

      <div v-if="error" class="w3-panel w3-red">
        <h3>Error!</h3>
        <p>Could not fetch movie data: {{ error }}</p>
      </div>

      <div v-else-if="movies.length === 0" class="w3-container">
        <p>No movies available.</p>
      </div>


      <div v-else v-for="movie in movies" :key="movie.id" class="w3-container w3-half w3-margin-bottom">
        <div class="w3-card-4">
          <div class="w3-container w3-center">
            <h3>{{ movie.title }}</h3>
            <h5>{{ movie.director.name }}</h5>
            <p>{{ movie.actors.map(a => a.name).join(', ') }}</p>
            <p>{{ movie.genres.map(g => g.name).join(', ') }}</p>
          </div>
        </div>
      </div>
    </div>

  </section>

</template>

<style scoped>
</style>