<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for="question in questions" :key="question.pk">
        <p class="mb-0">
          <span class="author-name">Posted by {{ question.author }}</span>
        </p>
        <h2>
          <router-link
              :to="{ name: 'question', params: { slug: question.slug }}"
              class="question-link"
          >
            {{ question.content }}
          </router-link>
        </h2>
        <p>Answers: {{ question.answers_count }}</p>
        <hr>
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
        <button
        v-show="next"
        @click="getQuestions"
        class="btn btn-sm btn-outline-success">
          Load more
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import {apiService} from "@/common/api.service";

export default {
  name: "Home",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false
    }
  },
  methods: {
    getQuestions() {
      let endpoint = 'api/questions/';
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
          .then(data => {
            this.questions.push(...data.results)
            this.loadingQuestions = false;
            if (data.next) {
              this.next = data.next;
            } else  {
              this.next = null;
            }
          })
    }
  },
  created() {
    this.getQuestions();
    document.title = 'QuestionTime';
  }
};
</script>

<style>
.author-name {
  font-weight: bold;
  color: #d75858;
}

.question-link {
  font-weight: bold;
  color: #000;
}

.question-link:hover {
  text-decoration: none;
  color: #343A40;
}
</style>