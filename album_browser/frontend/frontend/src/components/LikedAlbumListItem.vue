<!-- List item that populates the LikedModal with album information for liked albums-->

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
					<button @click="toggleLike" 
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
        // Add or remove album from the list of liked albums
			toggleLike() {
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