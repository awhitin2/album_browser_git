<template>
    <div class="list-group-item">
        <div class = 'container-fluid'>
            <div class = 'row align-items-center'>
                <div class = 'col-1'>      
                    <h6 class='text-light text-center'>{{ index }}</h6>
                </div>
                <div class = 'col'>     
                    <h6 class='text-left text-light'>{{ albumName }}</h6>
                </div>
                <div class = 'col-3 float-right'>
                    <h6 class='text-light'>{{ artistName }}</h6>
                </div>
                <div class = 'col-1'>
                    <button @click="like" 
                            type="button" 
                            class = 'btn'>
                                <i :class="[isLiked ? likedIcon : notLikedIcon]"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
  import Vue from "vue";
  import { store } from '@/store.js'

  export default {
    props: {
      albumName: { required: true, type: String },
      index: {required: true, type: Number},
      liked: {default: false, type: Boolean},
      artistName: {required: true, type: String},
    },
    data() {
      return {
        isLiked: this.albumName in store.likedAlbums,
        likedIcon: "bi bi-heart-fill text-danger",
        notLikedIcon: "bi bi-heart"
      };
    },
    methods: {
        like() {
            if (!this.isLiked){
                Vue.set(store.likedAlbums, this.albumName, this.artistName)                
            }
            else {
               Vue.delete(store.likedAlbums, this.albumName)
            }
            console.log(store.likedAlbums)
        }
    },
  };
</script>s