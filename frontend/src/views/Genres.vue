<script setup lang="js">
import {onMounted, ref} from "vue";

const genres = ref([]);
const error = ref(null);
const newGenreName = ref("");

onMounted(async () => {
  try {
    const response = await fetch("http://localhost:8181/api/v1/genres", {
      headers: {
        "Accept": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! ${response.status}`);
    }

    const data = await response.json();
    genres.value = data.genres;
    console.log(genres.value);

  } catch (e) {
    error.value = e.message;
    console.error("Failed to fetch genres:", e);
  }

});

async function addGenre() {
  if (!newGenreName.value.trim()) return;

  try {
    const response = await fetch("http://localhost:8181/api/v1/genres", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({name: newGenreName.value}),
    });

    if (!response.ok) {
      throw new Error(`Failed to add genre: ${response.status}`);
    }

    const genre = await response.json();
    genres.value.push({id: genre.id, name: genre.name});
    newGenreName.value = "";

  } catch (e) {
    error.value = e.message;
    console.error("Error adding genre:", e);
  }
}

const deleteGenre = (id) => {
  genres.value = genres.value.filter((g) => g.id !== id);
  // Later: replace with API call DELETE /api/v1/genres/{id} once backend supports it
};
</script>

<template>
  <section>
    <h3 class="w3-center">Genres</h3>
    <div class="w3-row-padding w3-section w3-stretch w3-center">
      <form @submit.prevent="addGenre">
        <div class="w3-half w3-container">
          <input
              v-model="newGenreName"
              class="w3-input w3-center w3-border w3-round w3-light-grey"
              type="text"
              placeholder="Genre Name"
          />
        </div>
        <div class="w3-half w3-container">
          <button class="w3-button w3-block w3-border w3-round w3-light-grey" type="submit">
            Add Genre
          </button>
        </div>
      </form>
    </div>

    <div v-if="error" class="w3-panel w3-red">
      <p>{{ error }}</p>
    </div>

    <div v-else class="w3-responsive">
      <table class="w3-table-all w3-centered w3-hoverable w3-card">
        <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Action</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="genre in genres" :key="genre.id">
          <td>{{ genre.id }}</td>
          <td>{{ genre.name }}</td>
          <td>
            <button class="w3-button w3-red w3-round" @click="deleteGenre(genre.id)">
              Delete
            </button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>
