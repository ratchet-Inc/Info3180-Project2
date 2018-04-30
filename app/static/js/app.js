/* Add your Application JavaScript */
var auth = false; var u_id=2;
var b1 = "/register"; var b1Msg = "Register"; var b2 = "/login"; var b2Msg = "Login";

Vue.component('app-header', {
    template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <a class="navbar-brand" href="#">Photogram</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto float-right">
          <li class="nav-item active">
            <router-link class="nav-link" to="/">Home <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item active">
            <router-link class="nav-link" to="/explore">Explore <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item active">
            <router-link class="nav-link" to="/myprofile">My Profile <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item active">
            <router-link class="nav-link" to="/logout">Logout <span class="sr-only">(current)</span></router-link>
          </li>
        </ul>
      </div>
    </nav>
    `
});

Vue.component('app-footer', {
    template: `
    <footer>
        <div class="container">
            <p>Copyright &copy; Flask Inc.</p>
        </div>
    </footer>
    `
});

const upload = Vue.component('upload', {
    template: `
    <form id="uploadForm" @submit.prevent="uploadPhoto" method="POST" enctype="multipart/form-data">
        <h3>Upload Form</h3>
        <label>Description of file:</label>
        <input type="text" name="description" size="100" />
        <br />
        <label>Upload Image File:</label>
        <input type="file" name="photo" />
        <br />
        <br />
        <button type="submit">Submit</button>
    </form>
    `,
    methods: {
        uploadPhoto: function () {
            let self = this;
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);

            fetch("/api/upload", {
                method: "POST",
                body: form_data,
                headers: {
                    'X-CSRFToken': token
                },
                credentials: 'same-origin'
            }).then(
                function (res) { return res.json(); }
                ).then(
                function (r) { self.msg = r }
                ).catch(
                function (er) { console.log(er); }
                );
        }
    },
    data: function () {
        return { msg:[] }
    }
});

const explore = Vue.component('explore', {
    template:`
    <div class="jumbotron">
        <h3>explore Place holder</h3>
        <div class="">
            <ul class="postList">
                <li class="postItem" style="visibility:hidden;">
                    <div class="info">
                        <p id="postername"></p>
                    </div>
                    <div class="picSect">
                        <img id="postImg" src="" alt="post image" />
                    </div>
                    <div class="captSec">
                        <p id="postCapt"></p>
                    </div>
                </li>
            </ul>
        </div>
    </div>
    `,
    methods: {
        func: function(){
            fetch("/api/posts",{
                method: "GET"
            }).then(function(res){
                return res.json();
            }).then(function(r){
                console.log(r);
                var l = document.getElementsByClassName("postList")[0];
                for(var x = 0; x < r.posts.length; x++){
                    var copy = document.getElementsByClassName("postItem")[0].cloneNode(true);
                    copy.style.visibility = "visible";
                    var n = copy.childNodes;
                    //console.log("n: "+n.length);
                    n[1].firstChild.src = "/static/posts/"+r.posts[x].image;
                    n[4].innerHTML = r.posts[x].caption;
                    l.appendChild(copy);
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    mounted: function(){
        this.func();
    },
    data: function() {
        return {}
    }
});

const login = Vue.component('login', {
    template:`
    <div class="jumbotron">
        <h3>Photogram Login</h3>
        <form id="loginForm" @submit.prevent="logForm" method="POST" enctype="multipart/form">
            <div class="formSect">
                <label for="username">Username:</label>
                <input type="text" name="username" />
            </div>
            <div class="formSect">
                <label for="password">Password:</label>
                <input type="password" name="password" />
            </div>
            <br />
            <button type="submit">Login</button>
        </form>
    </div>
    `,
    methods: {
        logForm: function() {
            let self = this;
            let upform = document.getElementById("loginForm");
            let formData = new FormData(upform)
            
            fetch("/api/auth/login", {
                method: "POST",
                body: formData,
                headers:{
                    'X-CSRFToken': token
                },
                credentials: 'same-origin'
            }).then(function(res){
                console.log(res);
                //router.go("/explore");
                return res.json();
            }).then(function(r){
                console.log(r);
                self.msg = r;
                if(r.msg == "success"){
                    console.log("success recieved");
                    //router.replace("/explore");
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    data: function() {
        return {}
    }
});

const logout = Vue.component('logout', {
    template:`
    <div class="jumbotron">
        <h3>logging out..</h3>
    </div>
    `,
    methods: {
        func: function(){
            fetch("/api/auth/logout",{
                method: "GET",
                credentials: 'same-origin'
            }).then(function(res){
                return res.json();
            }).then(function(r){
                if(r.status == "OK"){
                    router.replace("/");
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    mounted: function(){
        this.func();
    },
    data: function() {
        return {}
    }
});

const register = Vue.component('register', {
    template:`
    <div class="jumbotron">
        <h3>Photogram registration form</h3>
        <form id="registerForm" @submit.prevent="regForm" method="POST" enctype="multipart/form-data">
            <div class="formSect">
                <label for="userEmail">Email:</label>
                <input type="text" name="email" />
            </div>
            <div class="formSect">
                <label for="fname">First Name:</label>
                <input type="text" name="fname" />
            </div>
            <div class="formSect">
                <label for="lastName">Last Name:</label>
                <input type="text" name="lname" />
            </div>
            <div class="formSect">
                <label for="userName">Username:</label>
                <input type="text" name="username" />
            </div>
            <div class="formSect">
                <label for="passcode">Password:</label>
                <input type="password" name="passcode" />
            </div>
            <div class="formSect">
                <label for="passcodeC">Confirm Password:</label>
                <input type="password" name="passcodeC" />
            </div>
            <div class="formSect">
                <label for="location">Location:</label>
                <input type="text" name="location" />
            </div>
            <div class="formSect">
                <label for="bio">Biography:</label>
                <br />
                <textarea name="bio" placeholder="Your bio here" rows="5" cols="32"></textarea>
            </div>
            <div class="formSect">
                <label for="profilePicture">Profile Picture:</label>
                <input type="file" name="img" />
            </div>
            <br />
            <button type="submit">Submit</button>
        </form>
    </div>
    `,
    methods: {
        regForm: function() {
            let self = this;
            let upform = document.getElementById("registerForm");
            let formData = new FormData(upform)
            
            fetch("/api/users/register", {
                method: "POST",
                body: formData,
                headers:{
                    'X-CSRFToken': token
                },
                credentials: 'same-origin'
            }).then(function(res){
                return res.json();
            }).then(function(r){
                self.msg = r;
                console.log(r);
                if(r.msg == "success"){
                    router.replace("/");
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    data: function() {
        return { msg:[] }
    }
});

const newPost = Vue.component('npost', {
    template:`
    <div class="jumbotron">
        <h3>New Post</h3>
        <form id="postForm" @submit.prevent="postForm" method="POST" enctype="multipart/form-data">
            <div class="formSect">
                <label for="capt">Caption:</label>
                <input type="text" name="capt" />
            </div>
            <div class="formSect">
                <label for="photo">Password:</label>
                <input type="file" name="photo" />
            </div>
            <br />
            <button type="submit">Post</button>
        </form>
    </div>
    `,
    methods: {
        postForm: function() {
            let self = this;
            let upform = document.getElementById("postForm");
            let formData = new FormData(upform)
            
            fetch("/api/users/"+u_id+"/posts", {
                method: "POST",
                body: formData,
                headers:{
                    'X-CSRFToken': token
                },
                credentials: 'same-origin'
            }).then(function(res){
                console.log(res);
                //router.go("/explore");
                return res.json();
            }).then(function(r){
                console.log(r);
                self.msg = r;
                if(r.msg == "success"){
                    console.log("success recieved");
                    //router.replace("/explore");
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    data: function() {
        return {}
    }
});

const viewPost = Vue.component('vpost', {
    template:`
    <div class="jumbotron">
        <h3>post place holder</h3>
    </div>
    `,
    methods: {
    },
    data: function() {
        return {}
    }
});

const viewProfile = Vue.component('vprofile', {
    template:`
    <div class="jumbotron">
        <h3>Profile place holder</h3>
        <p id="userID" style="visibility:hidden;">{{ $route.params.id }}</p>
        <div class="infoSect">
            <div class="imgDiv">
                <img id="profPic" src="" alt="profile image" />
            </div>
            <div class="infoDetails1">
                <p id="nameP"></p>
                <p id="locP"></p>
                <p id="joinP"></p>
                <p id="bioP"></p>
            </div>
            <div class="infoDetails2">
                <p id="postsP">Posts: 0</p>
                <p id="followsP">Followers: 0</p>
                <button>Follow</button>
            </div>
        </div>
        <div class="postSect" style="visibility:hidden;">
            <div class="postImage">
                <img src="" alt="posted image" />
            </div>
        </div>
    </div>
    `,
    methods: {
        retr: function(){
            var x = document.getElementById("userID");
            fetch("/api/users/"+x.innerHTML+"/posts",{
                method: "GET"
            }).then(function(res){
                return res.json();
            }).then(function(r){
                console.log(r);
                document.getElementById("profPic").src = "/static/uploads/"+r.image;
                document.getElementById("nameP").innerHTML = r.fname+" "+r.lname;
                document.getElementById("locP").innerHTML = r.loc;
                document.getElementById("bioP").innerHTML = r.bio;
                document.getElementById("joinP").innerHTML = r.joined;
                var loc = document.getElementsByClassName("postSect")[0];
                for(var x = 0; x < r.posts.length; x++){
                    var copy = document.getElementsByClassName("postImage")[0].cloneNode(true);
                    copy.firstChild.src = "/static/posts/"+r.posts[x].image;
                    copy.firstChild.style.visibility = "visible";
                    loc.appendChild(copy);
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    mounted: function(){
        this.retr();
    },
    data: function() {
        return {}
    }
});

const myProfile = Vue.component('myprofile', {
    template:`
    <div class="jumbotron">
        <h3>Profile place holder</h3>
        <p id="userID" style="visibility:hidden;">{{ var1 }}</p>
        <div class="infoSect">
        </div>
        <div class="postSec">
        </div>
    </div>
    `,
    methods: {
        retr: function(){
            var x = document.getElementById("userID");
            fetch("/api/users/"+x.innerHTML+"/posts",{
                method: "GET"
            }).then(function(res){
                return res.json();
            }).then(function(r){
                console.log(r);
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    mounted: function(){
        this.retr();
    },
    data: function() {
        return {
            var1: u_id
        }
    }
});

const Home = Vue.component('home', {
   template: `
    <div class="jumbotron">
        <div id="picSect">
            <img src="/static/default/home bg.jpg" alt="example image" />
        </div>
        <div id="infoSect">
            <div>
                <img src="/static/default/instagram-logo2.png" alt="Camera Image" />
                <h3>Photogram</h3>
            </div>
            <div>
                <p>Share Photos on Photogram(fake insta)</p>
                <div class="regBtn">
                    <router-link class="nav-link" v-bind:to="route1">{{ r1 }}<span class="sr-only">(current)</span></router-link>
                </div>
                <div class="logBtn">
                    <router-link class="nav-link" :to="route2">{{ r2 }}<span class="sr-only">(current)</span></router-link>
                </div>
            </div>
        </div>
    </div>
   `,
   methods:{
       checkLogin: function(){
           if(!auth){
               let self = this;
               console.log("start2: "+auth);
               fetch("/api/auth/check").then(function(res){
                    return res.json();
                }).then(function(r){
                    self.msg = r;
                    auth = r.auth;
                    u_id = r.id;
                    console.log("name: "+r.name);
                    if(auth){
                        b1 = "/";
                        b1Msg = r.name;
                        b2 = "/logout";
                        b2Msg = "Logout";
                    }
                }).catch(function(er){
                    console.log("Error:"+er);
                });
           }
       }
   },
   mounted: function(){
       this.checkLogin();
   },
   data: function() {
       console.log("start1"+b1);
       return {
           r1: b1Msg,
           r2: b2Msg,
           route1: b1,
           route2: b2
       }
    }
});

// Define Routes
const router = new VueRouter({
    routes: [
        { path: "/", component: Home },
        { path: "/upload", component: upload },
        { path: "/explore", component: explore },
        { path: "/login", component: login },
        { path: "/logout", component: logout },
        { path: "/register", component: register },
        { path: "/posts/new", component: newPost },
        { path: "/users/:id", component: viewProfile },
        { path: "/myprofile", component: myProfile }
    ]
});

// Instantiate our main Vue Instance
let app = new Vue({
    el: "#app",
    router
});