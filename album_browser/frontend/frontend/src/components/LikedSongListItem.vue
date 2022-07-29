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
  import { store } from '@/store.js'

  export default {
    props: {
      songName: { required: true, type: String },
      index: {required: true, type: Number},
      liked: {default: false, type: Boolean},
      artistName: {required: true, type: String},
    },
    data() {
      return {
        isLiked: this.songName in store.likedSongs,
        likedIcon: "bi bi-heart-fill text-danger",
        notLikedIcon: "bi bi-heart"
      };
    },
    methods: {
        like() {
            this.isLiked = !this.isLiked
            if (this.isLiked){
                store.likedSongs[this.songName] = this.artistName
            }
            else {
               delete store.likedSongs[this.songName]
            }
            console.log(store.LikedSongs)
        }
    },
  };
</script>s