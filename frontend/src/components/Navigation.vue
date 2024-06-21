<script setup>
import  {RouterLink} from 'vue-router'

const items = ["Выйти"];

</script>

<template>
  <v-app-bar app>
    <!-- Link to main page. -->
    <v-toolbar-title>
      <RouterLink class="link" to="/">Главная</RouterLink>
    </v-toolbar-title>

    <v-spacer></v-spacer>

    <!-- Link to equipment creation page. -->
    <v-btn icon>
      <RouterLink class="link" to="/create">
        <v-icon>mdi-folder-plus</v-icon>
      </RouterLink>
    </v-btn>

    <!-- Account settings menu. -->
    <v-menu>
      <template v-slot:activator="{  props }">
        <v-btn v-bind="props">
            <v-icon>mdi-account</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item :key="index" :value="item" v-for="(item, index) in items">
          <v-list-item-title>{{ item }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

  </v-app-bar>
</template>


<style>
.link {
  color: black;
  text-decoration: none;
}
</style>