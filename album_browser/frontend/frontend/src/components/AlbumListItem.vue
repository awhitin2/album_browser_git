
<!-- List item that populates the HomeView with album information-->

<template>
	<div>
		<b-button class="list-group-item list-group-item-action"
							type='button' 
							v-b-modal='modalId'
							style="position: relative; z-index:1">
			<div class = 'container-fluid'>
				<div class = 'row align-items-center'>
					<div class = 'col-1'>      
						<h4 class='text-light text-center'>{{ index }}</h4>
					</div>
					<div class = 'col-1'>      
						<img :src="imgSrcSmall" class="img-thumbnail mx-auto d-block"></img>
					</div>
					<div class = 'col'>     
						<div class='row'> 
							<div class='col'>
								<h3 class='text-left text-light'>{{ albumName }}</h3>
								<h6 class='text-left text-light'>{{ artistName }}</h6>
							</div>
						</div>
					</div>
					<div class = 'col-1 text-center'>
						<button @click.stop="toggleLike" 
										type="button" 
										class = 'btn text-center'>
											<i :class="[isLiked ? likedIcon : notLikedIcon]"></i>
						</button>
					</div>
				</div>
			</div>
		</b-button>
		<album-details-modal  :modalId="modalId"
													:albumName = "albumName"
													:albumLink = "albumLink"
													:albumId = "albumId"
													:artistName = "artistName"
													:artistLink = "artistLink"
													:imgSrcLarge = "imgSrcLarge"
													:price = "price"
													:category = "category"
													:releaseDate = "releaseDate">
		</album-details-modal>
	</div>
</template>


<script>
  import Vue from "vue";
  import uniqueId from 'lodash.uniqueid';
  import AlbumDetailsModal from "@/components/AlbumDetailsModal.vue";
  import { store } from '@/store.js'

  export default {
    components: {
        AlbumDetailsModal,
    },
    props: {
      albumName: { required: true, type: String },
      albumLink: { required: true, type: String },
      albumId: { required: true, type: String },
      artistName: { required: true, type: String },
      artistLink: { required: true, type: String },
      imgSrcSmall: {required: true, type: String},
      imgSrcLarge: {required: true, type: String},
      price: {required: true, type: String},
      category: {required: true, type: String},
      releaseDate: {required: true, type: String},
      index: {required: true, type: Number}
    },
    data() {
      return {
        modalId: uniqueId('modal-'),
        likedIcon: "bi bi-heart-fill text-danger",
        notLikedIcon: "bi bi-heart"
      };
    },
    computed: {
      isLiked: function() {
        return this.albumName in store.likedAlbums
		}
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
</script>