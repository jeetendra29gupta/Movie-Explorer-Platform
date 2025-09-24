<script setup lang="js">
import {onMounted, ref} from "vue";

const directors = ref([]);
const error = ref(null);
const newDirectorName = ref("");

onMounted(async () => {
  try {
    const response = await fetch("http://localhost:8181/api/v1/directors", {
      headers: {
        "Accept": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! ${response.status}`);
    }

    const data = await response.json();
    directors.value = data.directors;
    console.log(directors.value);

  } catch (e) {
    error.value = e.message;
    console.error("Failed to fetch directors:", e);
  }

});

async function addDirector() {
  if (!newDirectorName.value.trim()) return;

  try {
    const response = await fetch("http://localhost:8181/api/v1/directors", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({name: newDirectorName.value}),
    });

    if (!response.ok) {
      throw new Error(`Failed to add director: ${response.status}`);
    }

    const director = await response.json();
    directors.value.push({id: director.id, name: director.name});
    newDirectorName.value = "";

  } catch (e) {
    error.value = e.message;
    console.error("Error adding director:", e);
  }
}

const deleteDirector = (id) => {
  directors.value = directors.value.filter((d) => d.id !== id);
  // Later: replace with API call DELETE /api/v1/directors/{id} once backend supports it
};
</script>

<template>
  <section>
    <h3 class="w3-center">Directors</h3>
    <div class="w3-row-padding w3-section w3-stretch w3-center">
      <form @submit.prevent="addDirector">
        <div class="w3-half w3-container">
          <input
              v-model="newDirectorName"
              class="w3-input w3-center w3-border w3-round w3-light-grey"
              type="text"
              placeholder="Director Name"
          />
        </div>
        <div class="w3-half w3-container">
          <button class="w3-button w3-block w3-border w3-round w3-light-grey" type="submit">
            Add Director
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
        <tr v-for="director in directors" :key="director.id">
          <td>{{ director.id }}</td>
          <td>{{ director.name }}</td>
          <td>
            <button class="w3-button w3-red w3-round" @click="deleteDirector(director.id)">
              Delete
            </button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>
