<template>
    <button class="list-group-item list-group-item-action">
        <div class = 'container-fluid float-left'>
            <div class = 'row align-items-center'>
            <div class = 'col-1 text-left '>      
                <h3 class='text-left'>{{ index }}</h3>
            </div>
            <div class = 'col-2'>      
                <img :src="imgSrc" class="img-thumbnail"></img>
            </div>
            <div class = 'col text-left'>      
                <h3 class='text-center'>{{ albumName }} -- Artist Name</h3>
            </div>
            <div class = 'col-1 ml-auto'>   
                <div class='row'>
                <div class = 'col'>
                    <i class="bi bi-heart-fill float-right"></i>  
                </div> 
                </div>
                <div class='row'>
                <div class = 'col'>
                    <i class="bi bi-share-fill float-right"></i>  
                </div> 
                </div>
            </div>
            </div>
        </div>
    </button>
</template>


<script>
  import uniqueId from 'lodash.uniqueid';

  export default {
    props: {
      albumName: { required: true, type: String },
      favorited: { default: false, type: Boolean },
      imgSrc: {required: true, type: String},
      index: {required: true, type: Number}
    },
    data() {
      return {
        isFavorited: this.favorited,
        id: uniqueId('album-')
    };
  }
  };
</script>

// <!-- Add icon library -->
// <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

// <!-- Use an element to toggle between a like/dislike icon -->
// <i onclick="myFunction(this)" class="fa fa-thumbs-up"></i>


// function myFunction(x) {
//   x.classList.toggle("fa-thumbs-down");
// }