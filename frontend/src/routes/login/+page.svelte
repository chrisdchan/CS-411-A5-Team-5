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
		gap-4
        flex-col
        border-2
"
>
	<label>
		<span
			class="
            w-32
            text-right
            mr-5
			"
		>
			Email:
		</span>
		<input
			type="text"
			bind:value={email}
			class="
            px-1
			border-2 rounded-sm
			"
		/>
	</label>
	<label>
		<span
			class="
            w-32
            text-right
            mr-5
			"
		>
			Password:
		</span>
		<input
			type="password"
			bind:value={password}
			class="
			border-2 rounded-sm
			px-1
			"
		/>
	</label>
	<button
		on:click={handleSubmit}
		class="
			h-12 w-40
			bg-sky-300/100
			border-white border-solid rounded-lg
			hover:bg-sky-400/100
			m-6
		">Log in</button
	>
</div>
