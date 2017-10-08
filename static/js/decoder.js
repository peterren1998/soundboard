var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
var source;

function str2ab(str) {
  var buf = new ArrayBuffer(str.length*2); // 2 bytes for each char
  var bufView = new Uint16Array(buf);
  for (var i=0, strLen=str.length; i < strLen; i++) {
    bufView[i] = str.charCodeAt(i);
  }
  return buf;
}

function decode(data) {
    data = str2ab(data);

    source = audioCtx.createBufferSource();
    audioCtx.decodeAudioData(data, function(buffer) {
        source.buffer = buffer;

        source.connect(audioCtx.destination);
        source.loop = true;
        },

        function(e){ console.log("Error with decoding audio data" + e.err); }
    );

    source.start(0);
}
