<template>
    <div>
      <nav>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Profile</a></li>
          <li><a href="#">Settings</a></li>
          <li><a href="#">Logout</a></li>
        </ul>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginMenu'
  }
  </script>
  
  <style scoped>
  nav {
    background-color: #004494;
    padding: 1rem;
  }
  
  ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: flex;
    gap: 1rem;
  }
  
  li {
    display: inline;
  }
  
  a {
    color: white;
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  </style>
  