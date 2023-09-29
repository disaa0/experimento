import { useState } from "react";
import "./App.css";
import { useForm } from "react-hook-form";
import * as math from "mathjs";
import { useEffect } from "react";

function App() {
  const [evaluationError, setEvaluationError] = useState(null);
  const [result, setResult] = useState(null);

  const {
    register,
    handleSubmit,
    formState: { errors },
    watch,
  } = useForm();

  useEffect(() => {
    if (watch.length === 0) {
      setEvaluationError(null);
    }
  }, [watch]);

  const onSubmit = (data) => {
    setEvaluationError(null);

    try {
      const expression = data.expression.trim();
      const evaluation = math.evaluate(expression);

      setResult(evaluation);
    } catch (error) {
      setEvaluationError(
        "Ocurrió un error al evaluar la expresión. Por favor, verifícala.",
      );
    }
  };

  return (
    <>
      <div className="flex h-full w-full flex-col items-center justify-between gap-4">
        <h1>Expresiones aritméticas</h1>
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="flex flex-col items-center gap-2"
        >
          <input
            {...register("expression", {
              required: {
                value: true,
                message: "Debes escribir una expresión aritmética.",
              },
              pattern: {
                value: /^[\d\+\-\*\/\(\)\s]+$/,
                message:
                  "La expresión solo puede contener números y los caracteres +, -, * y /.",
              },
            })}
            className="rounded-sm bg-gray-600 p-2"
          />
          <button type="submit" className="rounded-md bg-purple-600 px-4 py-2">
            Calcular
          </button>
        </form>
        {errors.expression && (
          <span className="w-40 rounded-md bg-white bg-opacity-70 p-1 text-center text-sm font-bold text-[#e91e63]">
            {errors.expression.message}
          </span>
        )}
        {evaluationError && (
          <span className="w-40 rounded-md bg-white bg-opacity-70 p-1 text-center text-sm font-bold text-[#e91e63]">
            {evaluationError}
          </span>
        )}
        {result && (
          <span className="w-40 rounded-md bg-white bg-opacity-70 p-1 text-center text-sm font-bold text-[#e91e63]">
            El resultado de la expresión es {result}
          </span>
        )}
      </div>
    </>
  );
}

export default App;
