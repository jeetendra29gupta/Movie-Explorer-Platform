<script setup lang="js">
import {onMounted, ref} from "vue";

const actors = ref([]);
const error = ref(null);
const newActorName = ref("");

onMounted(async () => {
  try {
    const response = await fetch("http://localhost:8181/api/v1/actors", {
      headers: {
        "Accept": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! ${response.status}`);
    }

    const data = await response.json();
    actors.value = data.actors;
    console.log(actors.value);

  } catch (e) {

    error.value = e.message;
    console.error("Failed to fetch actors:", e);

  }

});

const deleteActor = (id) => {
  actors.value = actors.value.filter((a) => a.id !== id);
  // Later: replace with API call DELETE /api/v1/actors/{id} once backend supports it
};

async function addActor() {
  if (!newActorName.value.trim()) return;

  try {
    const response = await fetch("http://localhost:8181/api/v1/actors", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({name: newActorName.value}),
    });
    if (!response.ok) {
      throw new Error(`Failed to add actor: ${response.status}`);
    }

    const actor = await response.json();
    actors.value.push({id: actor.id, name: actor.name});
    newActorName.value = "";

  } catch (e) {
    error.value = e.message;
    console.error("Error adding actor:", e);
  }
}
</script>

<template>
  <section>
    <div class="w3-row-padding w3-section w3-stretch w3-center">
      <form @submit.prevent="addActor">
        <div class="w3-half w3-container">
          <input
              v-model="newActorName"
              class="w3-input w3-center w3-border w3-round w3-light-grey"
              type="text"
              placeholder="Actor Name"
          />
        </div>
        <div class="w3-half w3-container">
          <button
              class="w3-button w3-block w3-border w3-round w3-light-grey"
              type="submit"
          >
            Add Actor
          </button>
        </div>
      </form>
    </div>

    <div v-if="error" class="w3-panel w3-red">
      <h3>Error!</h3>
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
        <tr v-for="actor in actors" :key="actor.id">
          <td>{{ actor.id }}</td>
          <td>{{ actor.name }}</td>
          <td>
            <button
                class="w3-button w3-red w3-round"
                @click="deleteActor(actor.id)"
            >
              Delete
            </button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<style scoped>
</style>
