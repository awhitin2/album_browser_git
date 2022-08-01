
<!-- List item that populates the AblumDetailsModal with song information-->

<template>
    <div class="list-group-item">
        <div class = 'container-fluid'>
            <div class = 'row align-items-center'>
                <div class = 'col-1'>      
                    <h6 class='text-light text-center'>{{ index }}</h6>
                </div>
                <div class = 'col'>     
                    <h6 class='text-left text-light'>{{ songName }}</h6>
                </div>
                <div class = 'col-1'>
                    <h6 class='text-light'>{{ duration }}</h6>
                </div>
                <div class = 'col-1'>
                    <button @click="toggleLike" 
                            type="button" 
                            class = 'btn'>
                                <i :class="[isLiked ? likedIcon : notLikedIcon]">
                            </i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import Vue from "vue";
  import uniqueId from 'lodash.uniqueid';
  import { store } from '@/store.js'

  export default {
    props: {
      songName: { required: true, type: String },
      index: {required: true, type: Number},
      duration: {required: true, type: String},
      liked: {default: false, type: Boolean},
      artistName: {required: true, type: String},
    },
    data() {
      return {
        isLiked: this.songName in store.likedSongs,
        id: uniqueId('song-'),
        likedIcon: "bi bi-heart-fill text-danger",
        notLikedIcon: "bi bi-heart"
      };
    },
    methods: {
        // Add or remove song from the list of liked albums
        toggleLike() {
            this.isLiked = !this.isLiked
            if (this.isLiked){
                Vue.set(store.likedSongs, this.songName, this.artistName)                
            }
            else {
               Vue.delete(store.likedSongs, this.songName)
            }
        }
    },
  };
</script>

