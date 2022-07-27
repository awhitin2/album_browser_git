<template>
  <div>

    <b-modal id="my-modal"
              size = xl
              hide-footer
              hide-header
              title='Album Name'>

      <div class='container-fluid'>
        <div class = 'row align-items-center'>
          <div class = 'col-3'>
            <img src='https://is4-ssl.mzstatic.com/image/thumb/Music125/v4/00/a2/43/00a24363-cf69-bfd2-a26a-a042d57ab141/075992719926.jpg/170x170bb.png'
                class="img-thumbnail">
            </img>
          </div>
          <div class = 'col'>
            <div class = 'row'>
              <h1 class='display-6 text-center'>Album Name</h1>
            </div>
            <div class = 'row'>
              <h4 class='text-center text-info'>Artist Name</h4>
            </div>
            <div class = 'row'>
              <h6 class='text-center text-light'>Category</h6>
            </div>
            <div class = 'row'>
              <h6 class='text-center text-light'>Release Date</h6>
            </div>
          </div>
          <div class = 'col-1 float-right'>
            <div class = 'row'>
              <p class='text-light'>Price:</p>
            </div>
            <div class = 'row'>
              <p class='text-info'>$6.99</p>
            </div>
          </div>
        </div>
        <br>
        <div class = 'row align-items-center'>
          <div class = 'col'>
            <div class="list-group" v-for='item in albums' :key='item.index'>
              <song-list-item  :index = 'item.index' 
                                :songName = 'item.songName'>
              </song-list-item>
            </div>
          </div>
        </div>
      </div>
    </b-modal>

  </div>
</template>

<script>
import SongListItem from "@/components/SongListItem.vue";

export default {
  name: "ModalView",
  components: {
    SongListItem,
  },
  data() {
    return {
      albums: [
        {
          index: 1,
          songName: 'Here comes the sun'
        },
        {
          index: 2,
          songName: 'Get Back'
        }
      ]
    };
  },
  methods : {
    say() {
      alert('worked')
    }
  },
}
</script>


      // <!-- Using value -->
    // <b-button type='button' 
    //           class='btn btn-success' 
    //           v-b-modal="'my-modal'">Show Modal</b-button>

    // <!-- The modal -->