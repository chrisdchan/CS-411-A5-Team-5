<script lang="ts">
	let email = '';
	let password = '';
	let confirmPassword = '';

	const handleSignUp = async () => {
		console.log('submit');
	};
</script>

<div>Signup Page</div>

<div
	class="flex flex-col
    items-center
    bg-slate-200
    gap-2
"
>
	<label class="">
		Email:
		<input type="text" bind:value={email} class="border rounded-sm" />
	</label>
	<label>
		Password:
		<input
			type="password"
			bind:value={password}
			class="
            px-1
        "
		/>
	</label>
	<label>
		Confirm Password:
		<input
			type="password"
			bind:value={confirmPassword}
			class="
        px-1
        "
		/>
	</label>

	<button
		on:click={handleSignUp}
		class="border-0 rounded-md
            bg-sky-200 hover:bg-sky-300
            text-slate-200
            h-12
        ">Sign Up</button
	>
</div>
