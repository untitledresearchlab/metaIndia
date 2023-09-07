using Kvant;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class sprayController : MonoBehaviour
{
    private Spray throttleSource;

    // Start is called before the first frame update
    void Start()
    {
        
        throttleSource = GetComponent<Spray>();

        //throttleSource.throttle = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if(throttleSource.throttle > 0)
        {
            StartCoroutine(ResetVariableAfterDelay(5.0f)); // Change 2.0f to your desired delay in seconds.

        }
    }

    // Coroutine to reset scriptA.myVariable after a delay.
    private IEnumerator ResetVariableAfterDelay(float delay)
    {
        yield return new WaitForSeconds(delay);

        // Reset scriptA.myVariable to 0 after the specified delay.
        throttleSource.throttle = 0;
    }
}
