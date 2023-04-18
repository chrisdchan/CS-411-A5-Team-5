<script lang="ts">
	import getDayDiff from '../utils/format';
	export let meeting: Meeting;

	let duration: string = getDayDiff(meeting.startDate, meeting.endDate);
</script>

<div class="border-2 rounded-md">
	<h2>{meeting.name}</h2>
	<div>{meeting.startDate}</div>
	<div>{duration}</div>
</div>
