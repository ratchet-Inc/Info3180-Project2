/* Add your Application JavaScript */
Vue.component('app-header', {
    template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <a class="navbar-brand" href="#">Photogram</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
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
    </div>
    `,
    methods: {
        func: function(){}
    },
    data: function() {
        return {}
    }
});

const login = Vue.component('login', {
    template:`
    <div class="jumbotron">
        <h3>login place holder</h3>
    </div>
    `,
    methods: {},
    data: function() {
        return {}
    }
});

const logout = Vue.component('logout', {
    template:`
    <div class="jumbotron">
        <h3>logout place holder</h3>
    </div>
    `,
    methods: {},
    data: function() {
        return {}
    }
});

const register = Vue.component('register', {
    template:`
    <div class="jumbotron">
        <h3>register place holder</h3>
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
                console.log(res);
                router.go('/');
                return res.json();
            }).then(function(r){
                self.msg = r;
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    data: function() {
        return {}
    }
});

const newPost = Vue.component('npost', {
    template:`
    <div class="jumbotron">
        <h3>post place holder</h3>
    </div>
    `,
    methods: {},
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
    methods: {},
    data: function() {
        return {}
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
                <p>Share Photos on Phogram(fake insta)</p>
                <div class="">
                    <router-link class="nav-link" to="/register">Register<span class="sr-only">(current)</span></router-link>
                </div>
                <div class="">
                    <router-link class="nav-link" to="/login">Login<span class="sr-only">(current)</span></router-link>
                </div>
            </div>
        </div>
    </div>
   `,
    data: function() {
       return {}
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
        { path: "/posts/new", component: newPost }
    ]
});

// Instantiate our main Vue Instance
let app = new Vue({
    el: "#app",
    router
});