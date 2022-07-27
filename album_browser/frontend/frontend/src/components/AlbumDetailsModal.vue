<template>
  <b-modal :id="modalId"
            size = xl
            hide-footer
            hide-header
            title='Album Name'>

    <div class='container-fluid'>
      <div class = 'row align-items-center'>
        <div class = 'col-3'>
          <img :src='imgSrcLarge'
              class="img-thumbnail">
          </img>
        </div>
        <div class = 'col'>
          <div class = 'row'>
            <h1 class='display-6 text-center'>{{albumName}}</h1>
          </div>
          <div class = 'row'>
            <h4 class='text-center text-info'>{{artistName}}</h4>
          </div>
          <div class = 'row'>
            <h6 class='text-center text-light'>{{category}}</h6>
          </div>
          <div class = 'row'>
            <h6 class='text-center text-light'>{{releaseDate}}</h6>
          </div>
        </div>
        <div class = 'col-1 float-right'>
          <div class = 'row'>
            <p class='text-light'>Price:</p>
          </div>
          <div class = 'row'>
            <p class='text-info'>{{price}}</p>
          </div>
        </div>
      </div>
      <br>
      <div class = 'row align-items-center'>
        <div class = 'col'>
          <div class="list-group" v-for='song in songs' :key='song.index'>
            <song-list-item  :index = 'song.index' 
                              :songName = 'song.songName'>
            </song-list-item>
          </div>
        </div>
      </div>
    </div>
  </b-modal>
</template>

<script>
import SongListItem from "@/components/SongListItem.vue";

export default {
  name: "ModalView",
  props: {
      modalId: { required: true, type: String },
      albumName: { required: true, type: String },
      albumLink: { required: true, type: String },
      artistName: { required: true, type: String },
      artistLink: { required: true, type: String },
      imgSrcLarge: {required: true, type: String},
      price: {required: true, type: String},
      category: {required: true, type: String},
      releaseDate: {required: true, type: String},
    },
  components: {
    SongListItem,
  },
  data() {
    return {
      songs: [
        {
          index: 1,
          songName: 'Here comes the sun'
        }
      ]
    };
  },
  // methods : {
    // getAlbums() {
    //     const path = 'http://localhost:5000/albums';
    //     axios.get(path)
    //     .then((res) => {
    //         console.log(res.data)
    //         console.log(typeof res.data)
    //         this.albums = res.data.albums;
    //         console.log(this.albums)
    //     })
    //     .catch((err)=> {
    //         console.error(err)
    //     })
    // }
  // },
  // created(){
  //     this.getAlbums();
  // }
}
</script>


      // <!-- Using value -->
    // <b-button type='button' 
    //           class='btn btn-success' 
    //           v-b-modal="'my-modal'">Show Modal</b-button>

    // <!-- The modal -->