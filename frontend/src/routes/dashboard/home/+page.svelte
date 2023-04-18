<script lang="ts">
	import MeetingCard from '../../../components/meetingCard.svelte';

	var myVideo = '/dance.mp4';
	export let data;
</script>

<!-- <div
	class="flex border-1 w-full
items-center flex-col
"
> -->
<!-- <h2>Your Videos</h2> -->
<!-- <video controls autoplay class="h-5/12 w-5/12">
		<source src={myVideo} type="video/mp4" />
		<track kind="captions" />
	</video> -->
<!-- </div> -->

<div
	class="grid grid-cols-6 gap-4 grid-rows-6
            mt-6 mb-6
            h-5/6
            "
>
	<div
		class="
        col-start-1 col-end-2
        row-start-1 row-end-7
        bg-slate-200
        flex justify-center
        "
	>
		<button
			class="
            bg-sky-300 text-slate-100
            rounded-md
            h-10 px-4
            align-center
            "
		>
			Add Meeting
		</button>
	</div>
	<div
		class="
        col-start-2 col-end-5
        row-start-2 row-end-7
        "
	>
		{#each data.meetings as meeting, i}
			<MeetingCard {meeting} />
		{/each}
	</div>
	<div
		class="
        row-start-1 row-end-7
        col-start-5 col-end-7"
	>
		Friends
	</div>
</div>
