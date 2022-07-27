<template>
  <div class="home">
    <div v-for='(item, index) in albums' :key='item.albumName'
    class="list-group">
      <album-list-item :index = 'index+1' :albumName = 'item.albumName' :imgSrc = 'item.imgSrc' :favorited = 'item.favorited'></album-list-item>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import AlbumListItem from "@/components/AlbumListItem.vue";

export default {
  name: "HomeView",
  components: {
    AlbumListItem,
  },
  data() {
    return {
      albums: [
        { 
          albumName: 'Album 1', 
          favorited: true,
          imgSrc: 'https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/9a/37/93/9a379323-ac8e-766d-0dec-f19d95a54766/810074421287.jpg/60x60bb.png',
 
        },
        { 
          albumName: 'Album 2', 
          favorited: false,
          imgSrc: 'https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/9a/37/93/9a379323-ac8e-766d-0dec-f19d95a54766/810074421287.jpg/60x60bb.png',
        },
        { 
          albumName: 'Album 3', 
          favorited: false,
          imgSrc: 'https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/9a/37/93/9a379323-ac8e-766d-0dec-f19d95a54766/810074421287.jpg/60x60bb.png',
        },
      ]
    };
  }
};
</script>
