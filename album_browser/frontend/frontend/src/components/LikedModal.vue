
// Songs un-liked from the like Modal do not disappear without adding another song from elsewhere


<template>
  <b-modal  id='liked-modal'
            size = xl
            hide-header
            hide-footer
            title='Album Name'>

    <div class='container-fluid'>
      <div class = 'row align-items-center'>
        <div class = 'col'>
          <h4 class='text-center'>Liked Albums</h4>
        </div>
      </div>
      
      <hr class='bg-light'>
      <h5 v-if='Object.keys(likedAlbums).length === 0' 
          class='text-warning'>You have not yet liked any albums</h5>
      <br>
      <div class = 'row align-items-center'>
        <div class = 'col'>
          <h4 class='text-center'>Liked Songs</h4>
        </div>
      </div>
      <hr class='bg-light'>
      <h5 v-if='Object.keys(likedSongs).length === 0' 
          class='text-warning'>You have not yet liked any songs
      </h5>
      <br>
      <div class = 'row align-items-center'>
        <div class = 'col'>
          
          <div class="list-group" v-for='(artist, song) of likedSongs'>
            <liked-song-list-item :index = '1' 
                                  :songName = 'song'
                                  :artistName = 'artist'>
            </liked-song-list-item>
          </div>
        </div>
      </div>
      <button class='btn btn-primary btn-block' type="button">Download</button>
    </div>
  </b-modal>
</template>


<script>
  import LikedSongListItem from "@/components/LikedSongListItem.vue";
  import { store } from '@/store.js'
  
  export default {
    name: "LikedModal",
    components: {
      LikedSongListItem
    },
    data() {
      return {
        likedSongs: store.likedSongs,
        likedAlbums: store.likedAlbums,
        noLikedAlbums: Object.keys(store.likedAlbums).length === 0,
      };  
    },
    methods: {
    },
  }

</script>


