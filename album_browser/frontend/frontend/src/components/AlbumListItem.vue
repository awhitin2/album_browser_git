<template>
    <div>
        <b-button   class="list-group-item list-group-item-action"
                    type='button' 
                    v-b-modal='modalId'>
            <div class = 'container-fluid'>
                <div class = 'row align-items-center'>
                    <div class = 'col-1'>      
                        <h4 class='text-light text-center'>{{ index }}</h4>
                    </div>
                    <div class = 'col-1'>      
                        <img :src="imgSrcSmall" class="img-thumbnail mx-auto d-block"></img>
                    </div>
                    <div class = 'col-1'>      
                        <button type="button" class="btn btn-primary z-index:10">Click</button>
                    </div>
                    <div class = 'col'>     
                        <div class='row'> 
                            <div class='col'>
                                <h3 class='text-left text-light'>{{ albumName }}</h3>
                                <h6 class='text-left text-light'>{{ artistName }}</h6>
                            </div>
                        </div>
                    </div>
                    <div class = 'col-1 ml-auto'>   
                        <div class='row'>
                            <div class = 'col'>
                                <i class="bi bi-heart float-right"></i>  
                            </div> 
                        </div>
                        <div class='row' width='100%'>
                            <div class = 'col'>
                                <i class="bi bi-share float-right"></i>  
                            </div> 
                        </div>
                    </div>
                </div>
            </div>
        </b-button>
        <album-details-modal    :modalId="modalId"
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
  import uniqueId from 'lodash.uniqueid';
  import AlbumDetailsModal from "@/components/AlbumDetailsModal.vue";

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
      favorited: { default: true, type: Boolean },
      imgSrcSmall: {required: true, type: String},
      imgSrcLarge: {required: true, type: String},
      price: {required: true, type: String},
      category: {required: true, type: String},
      releaseDate: {required: true, type: String},
      index: {required: true, type: Number}
    },
    data() {
      return {
        isFavorited: this.favorited,
        modalId: uniqueId('modal-')
    };
  }
  };
</script>