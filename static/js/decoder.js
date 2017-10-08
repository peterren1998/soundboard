var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
var source;
var enc = new TextEncoder("utf-8");

function decode(data) {
    data = enc.encode(data);
    audioCtx.decodeAudioData(data, function(buffer) {
        source.buffer = buffer;

        source.connect(audioCtx.destination);
        source.loop = true;
        },

        function(e){ console.log("Error with decoding audio data" + e.err); }
    );

    source.start(0);
}
