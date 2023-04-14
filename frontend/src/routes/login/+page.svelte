<script lang="ts">
	let email = '';
	let password = '';

	const handleSubmit = async (e) => {
		console.log('====================================');
		console.log('Submit');
		console.log('====================================');
	};
</script>

<div
	class="
        h-screen
        flex justify-center items-center
        flex-col
        border-2
"
>
	<label>
		Email:
		<input type="text" bind:value={email} />
	</label>
	<label>
		Password:
		<input type="password" bind:value={password} />
	</label>
	<button on:click={handleSubmit}>Log in</button>
</div>
