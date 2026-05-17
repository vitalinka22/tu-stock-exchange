<!-- 404 page -->

<template>
  <v-container fluid class="error-background d-flex align-center justify-center">

    <v-card
      width="500"
      class="pa-10 text-center error-card"
      rounded="xl"
      elevation="0"
    >


      <div class="error-code">404</div>

      <h1 class="text-h4 font-weight-bold mb-2">
        Page not found
      </h1>

      <p class="text-medium-emphasis mb-6">
        The page you are looking for doesn’t exist or may have been moved.
      </p>


      <v-btn
        to="/"
        color="indigo-darken-3"
        size="large"
        rounded="lg"
        variant="flat"
        class="text-none font-weight-bold"
      >
        Go back home
      </v-btn>

    </v-card>

  </v-container>
  
</template>

<style scoped>
.error-background {
  min-height: 100vh;
  background:
    radial-gradient(circle at top left, #e0e7ff, transparent 30%),
    radial-gradient(circle at bottom right, #c7d2fe, transparent 30%),
    #f5f7fb;
}

.error-card {
  border: 1px solid #ececec;
  box-shadow: 0 10px 40px rgba(0,0,0,0.08);
}

.error-code {
  font-size: 96px;
  font-weight: 800;
  line-height: 1;
  color: #283593;
  margin-bottom: 16px;
}
</style>

