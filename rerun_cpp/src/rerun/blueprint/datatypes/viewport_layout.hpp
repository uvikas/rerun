// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/blueprint/datatypes/viewport_layout.fbs".

#pragma once

#include "../../collection.hpp"
#include "../../result.hpp"

#include <cstdint>
#include <memory>

namespace arrow {
    class Array;
    class DataType;
    class StructBuilder;
} // namespace arrow

namespace rerun::blueprint::datatypes {
    /// **Datatype**: A view of a space.
    ///
    /// Unstable. Used for the ongoing blueprint experimentations.
    struct ViewportLayout {
        /// space_view_keys
        rerun::Collection<uint8_t> space_view_keys;

        /// tree
        rerun::Collection<uint8_t> tree;

        /// auto_layout
        bool auto_layout;

      public:
        ViewportLayout() = default;
    };
} // namespace rerun::blueprint::datatypes

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<blueprint::datatypes::ViewportLayout> {
        static constexpr const char Name[] = "rerun.blueprint.datatypes.ViewportLayout";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::StructBuilder* builder, const blueprint::datatypes::ViewportLayout* elements,
            size_t num_elements
        );

        /// Serializes an array of `rerun::blueprint:: datatypes::ViewportLayout` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const blueprint::datatypes::ViewportLayout* instances, size_t num_instances
        );
    };
} // namespace rerun