<template>
  <div id="app">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" 
          href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css" 
          integrity="sha384-nNK9n28pDUDDgIiIqZ/MiyO3F4/9vsMtReZK39klb/MtkZI3/LtjSjlmyVPS3KdN" 
          crossorigin="anonymous">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href=
"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" />
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <div class="container-fluid">
        <a class="navbar-brand" 
            href="#"><span 
            class="mb-0 h2">Top 100 Albums</span></a>
        <button type="button" 
                class="btn btn-success" 
                data-toggle="modal" d
                ata-target="#">Favorites</button>
      </div>
      
    </nav>
    <router-view />
  </div>
</template>

<style>

</style>

