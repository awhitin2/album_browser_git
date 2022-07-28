<template>
    <div class="list-group-item">
        <div class = 'container-fluid'>
            <div class = 'row align-items-center'>
                <div class = 'col-1'>      
                    <h6 class='text-light text-center'>{{ index }}</h6>
                </div>
                <div class = 'col'>     
                    <div class='row'> 
                        <div class='col'>
                            <h6 class='text-left text-light'>{{ songName }}</h6>
                        </div>
                    </div>
                </div>
                <div class = 'col-1'>
                    <h6 class='text-light'>{{ duration }}</h6>
                </div>
                <div class = 'col-1'>
                    <button type="button" class = 'btn' ><i class="bi bi-share"></i></button>
                </div>
                <div class = 'col-1'>
                    <button type="button" class = 'btn' >{{favorited}}</button>
                </div>
                <div class = 'col-1'>
                    <button type="button" class = 'btn' ><i class="bi bi-heart"></i></button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
  import uniqueId from 'lodash.uniqueid';

  export default {
    props: {
      songName: { required: true, type: String },
      index: {required: true, type: Number},
      duration: {required: true, type: String},
      favorited: {default: false, type: Boolean}
    },
    data() {
      return {
        isFavorited: this.favorited,
        id: uniqueId('song-')
      };
    },
  };
</script>

// <!-- Add icon library -->
// <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

// <!-- Use an element to toggle between a like/dislike icon -->
// <i onclick="myFunction(this)" class="fa fa-thumbs-up"></i>


// function myFunction(x) {
//   x.classList.toggle("fa-thumbs-down");
// }
