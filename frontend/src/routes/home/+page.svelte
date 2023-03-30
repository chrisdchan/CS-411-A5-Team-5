<script lang="ts">
    import SummaryPanel from "../../components/summaryPanel.svelte";

    var myVideo = '/dance.mp4'
</script>


<h1 class="text-slate-500 border-2 w-4/12 m-1">Welcome to the Home Page</h1>

<div class='flex border-1 w-full 
items-center flex-col
'>
    <h2>Your Videos</h2>
    <video controls autoplay class='h-5/12 w-5/12'>
        <source src={myVideo} type='video/mp4'/>
        <track kind="captions"/>
    </video>
</div>

<!-- <SummaryPanel></SummaryPanel> -->

