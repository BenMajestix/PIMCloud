<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4">
        <div class="list-group">
          <button 
            v-for="(email, index) in emails" 
            :key="index" 
            class="list-group-item list-group-item-action"
            :class="{ active: selectedEmailIndex === index }"
            @click="selectEmail(index)"
          >
            {{ email.subject }}
          </button>
        </div>
      </div>
      <div class="col-md-8">
        <div v-if="selectedEmail" class="card">
          <div class="card-header">
            <strong>{{ selectedEmail.subject }}</strong>
          </div>
          <div class="card-body">
            <p>{{ selectedEmail.content }}</p>
          </div>
        </div>
        <div v-else>
          <p>Please select an email to view its content.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      emails: [
        { subject: "Welcome to Webmail", content: "Thank you for signing up for our service." },
        { subject: "Weekly Newsletter", content: "Here's what happened this week..." },
        { subject: "Your Subscription Update", content: "Your subscription will expire soon." }
      ],
      selectedEmailIndex: null
    };
  },
  computed: {
    selectedEmail() {
      return this.selectedEmailIndex !== null ? this.emails[this.selectedEmailIndex] : null;
    }
  },
  methods: {
    selectEmail(index) {
      this.selectedEmailIndex = index;
    }
  }
};
</script>

<style scoped>
.container-fluid {
  height: 100vh;
}
.list-group {
  height: 100%;
  overflow-y: auto;
}
.card {
  height: 100%;
}
</style>
