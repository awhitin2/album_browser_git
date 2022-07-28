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
            <h1 class='display-6 text-center'><a class = 'text-white' :href='albumLink' target="_blank">{{albumName}}</a></h1>
          </div>
          <div class = 'row'>
            <h4 class='text-center'><a class = 'text-info' :href='artistLink' target="_blank">{{artistName}}</a></h4>
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
            <song-list-item :index = 'song.index' 
                            :songName = 'song.songName'
                            :duration = 'song.duration'>
            </song-list-item>
          </div>
        </div>
      </div>
    </div>
  </b-modal>
</template>

<script>
import axios from 'axios'
import SongListItem from "@/components/SongListItem.vue";

export default {
  name: "ModalView",
  props: {
      modalId: { required: true, type: String },
      albumName: { required: true, type: String },
      albumLink: { required: true, type: String },
      albumId: { required: true, type: String },
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
      songs: []
    };
  },
  methods : {
    getSongs() {
        const path = 'http://localhost:5000/songs';
        axios.get(path, { params: { answer: this.albumLink } })
        .then((res) => {
            this.songs = res.data.songs;
        })
        .catch((err)=> {
            console.error(err)
        })
    }
  },
  mounted(){
      this.getSongs();
  }
}
</script>

