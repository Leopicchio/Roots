# Roots

<div class="row">
  <div class="column">
    <img src="https://github.com/Leopicchio/Roots/blob/main/PCB_roots.png" alt="drawing" width="200"/>
  </div>
  <div class="column">
    <img src="https://github.com/Leopicchio/Roots/blob/main/sensor.png" alt="drawing" width="200"/>
  </div>
  <div class="column">
    <img src="https://github.com/Leopicchio/Roots/blob/main/setup_example.png" alt="drawing" width="200"/>
  </div>
   <div class="column">
    <img src="https://github.com/Leopicchio/Roots/blob/main/PCB_arthur.png" alt="drawing" width="200"/>
  </div>
</div>

/* Three image containers (use 25% for four, and 50% for two, etc) */
.column {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}


Welcome to the Roots project! 

We created a touch sensor which is capable of recognizing complex interactions with everyday objects, only through a single wire connection. Our sensor measures the electrical property of the object over a range of frequencies and sends the data to a remote device (for example a laptop) via Wifi. The data is analyzed with a simple machine learning technique to recognize where and how we are touching the object.

We designed everything from scratch, starting with the PCB and ending with the classification algorithm and the user interface (which was written with the Qt framework).
