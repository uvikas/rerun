// NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.
// Based on "crates/re_types/definitions/rerun/testing/datatypes/fuzzy.fbs"

#include "flattened_scalar.hpp"

#include <arrow/api.h>

namespace rerun {
    namespace datatypes {
        const std::shared_ptr<arrow::DataType> &FlattenedScalar::to_arrow_datatype() {
            static const auto datatype = arrow::struct_({
                arrow::field("value", arrow::float32(), false, nullptr),
            });
            return datatype;
        }

        arrow::Result<std::shared_ptr<arrow::StructBuilder>>
            FlattenedScalar::new_arrow_array_builder(arrow::MemoryPool *memory_pool) {
            if (!memory_pool) {
                return arrow::Status::Invalid("Memory pool is null.");
            }

            return arrow::Result(std::make_shared<arrow::StructBuilder>(
                to_arrow_datatype(),
                memory_pool,
                std::vector<std::shared_ptr<arrow::ArrayBuilder>>({
                    std::make_shared<arrow::FloatBuilder>(memory_pool),
                })
            ));
        }

        arrow::Status FlattenedScalar::fill_arrow_array_builder(
            arrow::StructBuilder *builder, const FlattenedScalar *elements, size_t num_elements
        ) {
            if (!builder) {
                return arrow::Status::Invalid("Passed array builder is null.");
            }
            if (!elements) {
                return arrow::Status::Invalid("Cannot serialize null pointer to arrow array.");
            }

            {
                auto element_builder =
                    static_cast<arrow::FloatBuilder *>(builder->field_builder(0));
                ARROW_RETURN_NOT_OK(element_builder->Reserve(num_elements));
                for (size_t elem_idx = 0; elem_idx < num_elements; elem_idx += 1) {
                    ARROW_RETURN_NOT_OK(element_builder->Append(elements[elem_idx].value));
                }
            }
            ARROW_RETURN_NOT_OK(builder->AppendValues(num_elements, nullptr));

            return arrow::Status::OK();
        }
    } // namespace datatypes
} // namespace rerun