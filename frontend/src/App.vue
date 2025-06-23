<template>
  <div class="app">
    <h1>AI Tutor</h1>

    <div>
      <label>Chapter:</label>
      <select v-model="chapter">
        <option disabled value="">Select Chapter</option>
        <option>1 - Motion</option>
        <option>2 - Velocity and Acceleration</option>
        <option>3 - Newton's Laws</option>
      </select>
    </div>

    <div>
      <label>Section:</label>
      <select v-model="section">
        <option disabled value="">Select Section</option>
        <option>a - Theory</option>
        <option>b - Examples</option>
        <option>c - Problems</option>
      </select>
    </div>

    <div>
      <label>Your Question:</label>
      <textarea v-model="question" placeholder="Ask something..."></textarea>
    </div>

    <button @click="askAI" :disabled="loading">
      {{ loading ? "Asking..." : "Ask AI" }}
    </button>

    <div v-if="answer">
      <h2>AI Response:</h2>
      <p>{{ answer }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      chapter: "",
      section: "",
      question: "",
      answer: "",
      loading: false,
    };
  },
  methods: {
    async askAI() {
      if (!this.chapter || !this.section || !this.question) {
        alert("Please fill all fields");
        return;
      }

      this.loading = true;
      try {
        const response = await axios.post("http://localhost:8000/ask", {
          chapter: this.chapter,
          section: this.section,
          question: this.question,
        });

        this.answer = response.data.answer;
      } catch (err) {
        this.answer = "Error: " + (err.response?.data?.detail || err.message);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.app {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
  font-family: sans-serif;
}
textarea {
  width: 100%;
  height: 80px;
}
button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
}
</style>
